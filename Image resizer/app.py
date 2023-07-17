from PIL import Image

def resize_image(size1, size2):
    image = Image.open('concert4.jpg')
    print(f"current size: {image.size}")
    resized_image = image.resize((size1, size2))
    resized_image.save("newimage" + str(size1)+  ".jpg")
    
size1 = int(input("ENTER WIDTH: "))
size2 = int(input("ENTER HEIGHT: "))

resize_image(size1, size2)