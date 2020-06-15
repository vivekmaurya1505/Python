import pyqrcode
import png
from pyqrcode import QRCode

s = "https://web.whatsapp.com/"
url = pyqrcode.create(s)
url.png("myqrcode.png",scale = 6)
