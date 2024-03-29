import io
import uuid

import qrcode
from django.core.files import File
from PIL import Image


def generate_uuid() -> str:
    """
    Generate a UUID for a new employee.

    :return: A UUID.
    """
    # Generate a UUID for the employee
    return uuid.uuid4().hex


def generate_qrcode(information: str):
    """
    Generate a QR code for the given information.
    
    :param information: The information to be encoded in the QR code.
    :return: The QR code image.
    """
    
    # Create a QR code instance & make the QR code image from the data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(information)
    qr.make(fit=True)
    qrcode_img = qr.make_image(fill_color="black", back_color="white")
    
    # Calculate dimension to center the QR code
    width, height = qrcode_img.size
    canvas_dim = 500
    x = (canvas_dim - width) / 2
    y = (canvas_dim - height) / 2

    # Create a canvas where we will draw the QR code
    canvas = Image.new("RGB", (500, 500), "white")
    canvas.paste(qrcode_img, (int(x), int(y)))

    # Generate a bytes buffer to save the image
    buffer = io.BytesIO()
    canvas.save(buffer, format="PNG")
    canvas.close()
    
    return File(buffer)
