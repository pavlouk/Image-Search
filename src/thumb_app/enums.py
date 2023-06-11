from enum import Enum


class OrientationEnum(str, Enum):
    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"
    SQUARISH = "squarish"


class ColorEnum(str, Enum):
    BLACK_AND_WHITE = "black_and_white"
    BLACK = "black"
    WHITE = "white"
    YELLOW = "yellow"
    ORANGE = "orange"
    RED = "red"
    PURPLE = "purple"
    MAGENTA = "magenta"
    GREEN = "green"
    TEAL = "teal"
    BLUE = "blue"
