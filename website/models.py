import io
import qrcode
from django.core.files import File
from django.db import models
from PIL import Image

from website.utils import generate_uuid


class DataInformation(models.Model):
    uuid = models.CharField(
        max_length=100, editable=False, primary_key=True, default=generate_uuid
    )
    text_data = models.TextField(unique=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid
    
    def save(self, *args, **kwargs):
        # Create a QR code instance & make the QR code image from the data
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.text_data)
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

        # Set the image to the QR code field
        filename = f"qrcode-{self.uuid}.png"
        self.qr_code.save(filename, File(buffer), save=False)
        canvas.close()
        
        super().save(*args, **kwargs)
