import pyqrcode
from pyqrcode import QRCode
import png

website_link = "https://www.google.com"
qr_code = pyqrcode.create(website_link)

with open('website_qr_code.png', 'wb') as png_file:
    qr_code.png(png_file, scale=8)
