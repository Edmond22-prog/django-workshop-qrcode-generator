import base64
import io
import uuid

import qrcode


def generate_uuid() -> str:
    """
    Generate a UUID for a new employee.

    :return: A UUID.
    """
    # Generate a UUID for the employee
    return uuid.uuid4().hex


def generate_qr_code(data: str):
    """
    Generate QR code from data.

    :param data: The data to be encoded in the QR code.
    :return: The QR code image.
    """
    # Create a QR code instance & make the QR code image from the data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    img_bytes = buf.getvalue()

    # Convert the image to base64
    img_base64 = base64.b64encode(img_bytes).decode()

    return img_base64
