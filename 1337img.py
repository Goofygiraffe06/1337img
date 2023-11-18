from PIL import Image
img = Image.open('image.png').convert('L')
img.save('grey.png')
img.show()
