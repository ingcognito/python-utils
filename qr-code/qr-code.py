import qrcode

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
img = qr.make_image(fill_color="red", back_color="#23dda0")
img.save('./qrcode-' + s + '.png')
print(f"QR code saved as qrcode{s}.png")

