import cv2
import os

files = os.listdir("data")
print(files)

for file in files:
    image = cv2.imread(f"data\\{file}")

    y = 45
    x = 130
    h = 295
    w = 1280
    crop_image = image[y:h, x:w]

    cv2.imwrite(f"output\\{file[:-4]}.bmp", crop_image)
