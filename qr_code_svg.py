import qrcode.image.svg  # Импорт фабрики SVG-изображений

# Получаем данные от пользователя
data = input("Введите ссылку или текст: ")

# Указываем SVG-фабрику
factory = qrcode.image.svg.SvgImage

# Создаём QR-код с SVG-выводом
img = qrcode.make(data, image_factory=factory)

# Сохраняем изображение в файл
img.save("my_qr_code.svg")

# Уведомление об успехе
print("✅ SVG-файл успешно сохранён!")