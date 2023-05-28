from typing import Optional

from pydantic import BaseModel

from thumb_app.enums import ColorEnum, OrientationEnum


class SearchBase(BaseModel):
    query: str
    color: Optional[ColorEnum] = None
    orientation: Optional[OrientationEnum] = None
