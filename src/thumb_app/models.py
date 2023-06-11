from sqlalchemy import Column, Integer, String

from thumb_app.database import Base


class Thumbnail(Base):
    __tablename__ = "thumbnails"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    thumbnail_image = Column(String, index=True)
