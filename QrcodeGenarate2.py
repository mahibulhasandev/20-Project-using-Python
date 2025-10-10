import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)

qr.add_data("https://github.com/mahibulhasandev")
qr.make(fit=True)
img = qr.make_image(fill_color= "black", back_color="white")
img.save("github_Profile.png")