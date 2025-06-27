from PIL import Image

image=Image.open('cat.jpg')

resized_image=image.resize((200,150))

resized_image.save("small_cats.jpg")