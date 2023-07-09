import json
import secrets
from io import BytesIO

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import Response
from PIL import Image
from sqlalchemy.orm import Session

from thumb_app import settings
from thumb_app.client import fetch_image
from thumb_app.database import Base, SessionLocal, engine
from thumb_app.models import Thumbnail
from thumb_app.schemas import SearchBase
from thumb_app.utils import create_thumbnail

ENCODING_CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

app = FastAPI()
Base.metadata.create_all(bind=engine)


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
async def image_search(search: SearchBase, db: Session = Depends(get_db)):
    try:
        thumbnail_urls = json.loads(await fetch_image(search))
    except HTTPException:
        raise HTTPException(400)

    search_results = thumbnail_urls.get("results", [])
    if search_results:
        urls = search_results.pop().get("urls")
        raw_url = urls.get("small", "Error")
    else:
        raise HTTPException(400)

    try:
        image_buffer = BytesIO(await fetch_image(raw_url).content)
        thumbnail_string = create_thumbnail(Image.open(image_buffer), BytesIO())
    except HTTPException:
        raise HTTPException(400)

    generated_key = "".join(secrets.choice(ENCODING_CHOICES) for _ in range(5))
    db_thumbnail = Thumbnail(
        thumbnail_image=thumbnail_string,
        key=generated_key,
    )
    db.add(db_thumbnail)
    db.commit()
    db.refresh(db_thumbnail)

    return {"Access your thumbnail at: ": f"{settings.BASE_URL}/{generated_key}"}


@app.get("/search/{thumbnail_key}")
def show_thumbnail(thumbnail_key: str, request: Request, db: Session = Depends(get_db)):
    try:
        db_thumbnails = (
            db.query(Thumbnail).filter(Thumbnail.key == thumbnail_key).first()
        )
        if db_thumbnails:
            return Response(db_thumbnails.thumbnail_image, media_type="image/jpeg")

        raise HTTPException(status_code=400, detail=f"{thumbnail_key=} not found")
    except HTTPException:
        raise HTTPException(status_code=500, detail="internal error")
