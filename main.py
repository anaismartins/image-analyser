import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from PIL import Image

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

    gray = np.flip(gray, 0)

    hsumup = [0] * len(gray)
    vsumup = [0] * len(gray[0])

    #
    # print (len(gray), " - ", len(gray[0]))

    for column in range(len(gray)):
        for line in range(len(gray[column])):
            hsumup[column] += int(gray[column][line])
            vsumup[line] += int(gray[column][line])

    figure(figsize=(2.95, 2.95), dpi=100)
    plt.plot(hsumup, np.arange(len(gray)), linewidth=1)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f"output\\{file[:-4]}_hsumup.png", bbox_inches="tight", pad_inches=0)
    plt.clf()

    # print (vsumup)

    figure(figsize=(12.80, 2.95), dpi=100)
    plt.plot(vsumup, linewidth=1)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f"output\\{file[:-4]}_vsumup.png", bbox_inches="tight", pad_inches=0)
    plt.clf()

    original_image = Image.open(f"output\\{file[:-4]}.bmp")
    hsumup_image = Image.open(f"output\\{file[:-4]}_hsumup.png")
    vsumup_image = Image.open(f"output\\{file[:-4]}_vsumup.png")

    combined = Image.new(
        "RGB",
        (
            original_image.width + hsumup_image.width,
            original_image.height + vsumup_image.height,
        ),
        (255, 255, 255, 255),
    )
    combined.paste(original_image, (0, 0))
    combined.paste(hsumup_image, (original_image.width, 0))
    combined.paste(vsumup_image, (0, original_image.height))

    combined.save(f"output\\{file[:-4]}_combined.png")
