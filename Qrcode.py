import qrcode
from PIL import Image


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=5)

qr.add_data("https://github.com/harsh2772?tab=repositories")

qr.make(fit=True)

img = qr.make_image(back_color="white", fill_color="black")         # If you want to change the colours so you want to import PIL module and int the module you only use of Image.

img.save("Code.png")

# Another Way

# qr = qrcode.make('Some data here')
# type(qr)
# qr.save("Code_1.png")
