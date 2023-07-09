from io import BytesIO

from PIL import Image


def create_thumbnail(image: Image.Image, buffered_output: BytesIO):
    image.thumbnail(
        size=(200, image.height * 200 // image.width), resample=Image.Resampling.LANCZOS
    )
    image.save(buffered_output, format=image.format)
    return buffered_output.getvalue()
