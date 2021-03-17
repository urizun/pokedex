from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400,400))
new_img.save('thumbnail.jpeg') 
print(img.size)