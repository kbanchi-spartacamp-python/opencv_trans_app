import cv2
from PIL import Image

# otahuku_img = Image.open("images/kamen.jpg")
# otahuku_img.show()

# print(otahuku_img.split())

# otahuku_img.split()[0].show()
# otahuku_img.split()[1].show()
# otahuku_img.split()[2].show()
# otahuku_img.split()[3].show()

# otahuku_img = cv2.imread("images/kamen.jpg")
otahuku_img = cv2.imread("images/kamen_alpha.png", -1)
print(otahuku_img)
print(otahuku_img.shape)
