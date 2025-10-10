import qrcode as qr

img = qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg")
img.save("Qrcode_Save.png")