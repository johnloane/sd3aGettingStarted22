from PIL import Image, ImageFilter

before = Image.open("dkit.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")