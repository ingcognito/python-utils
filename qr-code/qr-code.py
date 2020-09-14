import qrcode
from datetime import date

s = input("Input a URL: ")

if s=="":
    print("Please enter a URL")
    exit(0)

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)
qr.add_data(s)
qr.make()
img = qr.make_image(fill_color="black", back_color="white")
img.save('./qrcode.png')
print("QR code has been saved as PNG.")

