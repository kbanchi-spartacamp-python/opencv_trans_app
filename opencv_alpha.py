import cv2

original_mask_img = "images/otahuku.png"

img_rgb = cv2.imread(original_mask_img)
# img_rgba = cv2.imread(original_mask_img, -1)
img_rgba = cv2.imread(original_mask_img, flags=cv2.IMREAD_UNCHANGED)

print(img_rgb.shape)
print(img_rgba.shape)

print(img_rgb[0][0])
print(img_rgba[0][0])

b = img_rgba[:, :, 0]
g = img_rgba[:, :, 1]
r = img_rgba[:, :, 2]
a = img_rgba[:, :, 3]

# cv2.imshow("image", img_rgba)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)
# cv2.imshow("a", a)
# cv2.destroyAllWindows()

img_rgb = img_rgba[:, :, :3]
mask1 = img_rgba[:, :, 3]
mask3 = cv2.merge((mask1, mask1, mask1))

print(mask3[0][0])
