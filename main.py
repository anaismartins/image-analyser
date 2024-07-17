import cv2

image = cv2.imread("data\\1.png")

y = 45
x = 130
h = 295
w = 1280
crop_image = image[y:h, x:w]

cv2.imwrite("output\\image.bmp", crop_image)
