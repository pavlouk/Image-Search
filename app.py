import secrets

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import Response
from sqlalchemy.orm import Session

from thumb_app import models
from thumb_app import schemas
from thumb_app.config import get_settings
from thumb_app.database import SessionLocal, engine
from thumb_app.external import fetch_image, unsplash_builder

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
ENCODING_CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return "Welcome to the unofficial Unsplash thumbnails API!"


@app.post("/search")
async def image_search(search: schemas.SearchBase, db: Session = Depends(get_db)):
    if not unsplash_builder(search):  # type: ignore
        raise HTTPException(status_code=400, detail="Your provided query is not valid")
    
    thumbnail_string = await fetch_image(unsplash_builder(search))
    key = "".join(secrets.choice(ENCODING_CHOICES) for _ in range(5))
    
    db_thumbnail = models.Thumbnail(thumbnail_image=thumbnail_string, key=key)
    db.add(db_thumbnail)
    db.commit()
    db.refresh(db_thumbnail)

    return {"Access your thumbnail at: ": f"{get_settings().base_url}/{key}"}  # type: ignore


@app.get("/{thumbnail_key}")
def show_thumbnail(thumbnail_key: str, request: Request, db: Session = Depends(get_db)):
    try: 
        db_thumbnails = db.query(models.Thumbnail).filter(models.Thumbnail.key == thumbnail_key).first()  # type: ignore
        if db_thumbnails:
            return Response(db_thumbnails.thumbnail_image, media_type="image/jpeg")  # type: ignore

        raise HTTPException(status_code=400, detail=f"{thumbnail_key=} not found")
    except:
        raise HTTPException(status_code=500, detail="internal error")
