import qrcode
text = input("Masukan Text: ")
png = '.png'
qr = qrcode.make(text)
qr.save(text + png)