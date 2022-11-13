import cv2
from PIL import Image

original_face_img = "images/man.png"
# original_face_img = "images/satou.jpg"
original_mask_img = "images/otahuku.png"


def find_face():
    # 顔検出の分類器を用意
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = cv2.imread(original_face_img)
    face_list = cascade.detectMultiScale(img)
    return face_list


def paste_img(face_list):
    x = face_list[0][0]
    y = face_list[0][1]
    w = face_list[0][2]
    h = face_list[0][3]
    face_img = Image.open(original_face_img)
    mask_img = Image.open(original_mask_img)
    resized_mask_img = mask_img.resize((w, h))
    resized_mask_img.save("images/resize_otahuku_pillow.png")
    resized_mask_img.split()[0].save("images/resize_otahuku_pillow_r.png")
    resized_mask_img.split()[1].save("images/resize_otahuku_pillow_g.png")
    resized_mask_img.split()[2].save("images/resize_otahuku_pillow_b.png")
    resized_mask_img.split()[3].save("images/resize_otahuku_pillow_a.png")
    face_img.paste(resized_mask_img, (x, y), resized_mask_img.split()[3])
    face_img.save("images/hensin_pillow.png")


face_list = find_face()
paste_img(face_list)
