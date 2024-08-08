"""
QR-URL TOOL
AUTHOR: mcuser
DATE: 08/2024
Version: 1
pip install pyqrcode pypng pillow
"""

import pyqrcode
from PIL import Image

print("Generate QR code")
link = input("Enter text/url: ")

# Generate QR code
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)

# Open and display the QR code image
image = Image.open("QRCode.png")
image.show()  # Use .show() to display the image