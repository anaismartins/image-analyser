import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

files = os.listdir("data")

for file in files:
    image = cv2.imread(f"data\\{file}")

    y = 45
    x = 130
    h = 295
    w = 1280
    crop_image = image[y:h, x:w]

    # add white borders of 10 pixels
    crop_image_borders = cv2.copyMakeBorder(
        crop_image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255]
    )

    cv2.imwrite(f"output\\{file[:-4]}.bmp", crop_image_borders)

    # [gray]
    # Transform source image to gray if it is not already
    if len(crop_image.shape) != 2:
        gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
    else:
        gray = crop_image

    gray = np.flip(gray, 0)

    hsumup = [0] * len(gray)
    vsumup = [0] * len(gray[0])

    for column in range(len(gray)):
        for line in range(len(gray[column])):
            hsumup[column] += int(gray[column][line])
            vsumup[line] += int(gray[column][line])

    # Horizontal sum plot
    dpi = 100
    hsumup_width = 2.95 * dpi
    hsumup_height = 2.95 * dpi

    fig_hsumup, ax_hsumup = plt.subplots(
        figsize=(hsumup_width / dpi, hsumup_height / dpi), dpi=dpi
    )
    ax_hsumup.plot(hsumup, np.arange(len(gray)), linewidth=1)
    ax_hsumup.axis("off")

    # Remove margins and tight layout
    ax_hsumup.margins(0)
    ax_hsumup.xaxis.set_major_locator(plt.NullLocator())
    ax_hsumup.yaxis.set_major_locator(plt.NullLocator())

    fig_hsumup.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig_hsumup.savefig(
        f"output\\{file[:-4]}_hsumup.png", dpi=dpi, bbox_inches="tight", pad_inches=0
    )
    plt.close(fig_hsumup)

    # Vertical sum plot
    vsumup_width = 12.80 * dpi
    vsumup_height = 2.95 * dpi

    fig_vsumup, ax_vsumup = plt.subplots(
        figsize=(vsumup_width / dpi, vsumup_height / dpi), dpi=dpi
    )
    ax_vsumup.plot(vsumup, linewidth=1)
    ax_vsumup.axis("off")

    # Remove margins and tight layout
    ax_vsumup.margins(0)
    ax_vsumup.xaxis.set_major_locator(plt.NullLocator())
    ax_vsumup.yaxis.set_major_locator(plt.NullLocator())

    fig_vsumup.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig_vsumup.savefig(
        f"output\\{file[:-4]}_vsumup.png", dpi=dpi, bbox_inches="tight", pad_inches=0
    )
    plt.close(fig_vsumup)

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
