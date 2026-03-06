import qrcode


data = input("Введите ссылку: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Генерация изображения с настроенными цветами
img = qr.make_image(
    fill_color="#FF1493",
    back_color="black"
)

# Открытие изображения
img.show()

# Сохраняем изображение в файл
img.save("my_qr_code.png")

# Сообщаем об успехе
print("✅ QR-код успешно создан!")