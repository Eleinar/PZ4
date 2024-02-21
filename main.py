from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'black')
idraw = ImageDraw.Draw(img)
idraw.rectangle((0,0,100,100), fill = 'white')
img.save('test2.jpg')
img = Image.open('test2.jpg')
img.show()