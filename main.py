from PIL import Image, ImageDraw, ImageFont
img = Image.open('/home/KHPK.RU/student/Рабочий стол/Жыпеги/КОМПЬЮТЕР 1.jpeg') # открываем изображение

img = Image.new('RGB', (200, 200), 'black')
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()