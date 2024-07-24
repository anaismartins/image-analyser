import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

files = os.listdir("data")

for file in files:
    image = cv2.imread(f"data\\{file}")

    y = 45
    x = 130
    h = 295
    w = 1280
    crop_image = image[y:h, x:w]

    cv2.imwrite(f"output\\{file[:-4]}.bmp", crop_image)

    # [gray]
    # Transform source image to gray if it is not already
    if len(crop_image.shape) != 2:
        gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
    else:
        gray = crop_image

    hsumup = [0] * len(gray)
    vsumup = [0] * len(gray[0])

    #
    #print (len(gray), " - ", len(gray[0]))

    for column in range(len(gray)):
        for line in range(len(gray[column])):
            hsumup[column] += int(gray[column][line])
            vsumup[line] += int(gray[column][line])


    plt.plot(hsumup, np.arange(len(gray)), linewidth=1)
    plt.savefig(f"output\\{file[:-4]}_hsumup.png")
    plt.clf()

    #print (vsumup)

    plt.plot(vsumup, linewidth=1)
    plt.savefig(f"output\\{file[:-4]}_vsumup.png")
    plt.clf()