import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

files = os.listdir("data")

for file in files:
    image = cv2.imread(f"data\\{file}")

    y = 45
    x = 132
    h = 45+650
    w = 132+1280
    crop_image = image[y:h, x:w]

    cv2.imwrite(f"output\\{file[:-4]}.bmp", crop_image)

# Imagem em branco
img = np.ones((650+20, 1280+20, 3), dtype = np.uint8)
img = 255* img

img.add(crop_image, img)

# display the image using opencv
#cv2.imshow('black image', img)
cv2.imwrite(f"output\\white.bmp", img)
#cv2.waitKey(0)
