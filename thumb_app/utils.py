from io import BytesIO

from PIL import Image


def create_thumbnail(buffered_image: BytesIO):
    image = Image.open(buffered_image)
    image.thumbnail(
        size=(200, image.height * 200 // image.width), resample=Image.Resampling.LANCZOS
    )
    buffered_output = BytesIO()
    image.save(buffered_output, format=image.format)
    thumbnail_string = buffered_output.getvalue()
    return thumbnail_string
