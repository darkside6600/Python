import qrcode

def generate_qrcode(text);
	qr = qrcode.QRCode(
		version = 1,
error_correction = qrcode.constants.ERROR_CORRECT_l,
box_size = 10,
border = 4,
)
	qr.add_data(text)
	qr.make(fit=true)
	img = qr.make_image(fill_color="black", back_color="white")
	img.save("qrimg001.png")


url = input ("Enter your url:/ ")
generage_qrcode(url)