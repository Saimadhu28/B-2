import os

def get_image_pairs(image_folder):

    pairs = []

    files = sorted(os.listdir(image_folder))

    pre_images = {}

    # Find all pre-disaster images
    for file in files:

        if "_pre_disaster.png" in file:

            key = file.replace("_pre_disaster.png", "")

            pre_images[key] = file

    # Match each post image with its corresponding pre image
    for file in files:

        if "_post_disaster.png" in file:

            key = file.replace("_post_disaster.png", "")

            if key in pre_images:

                pairs.append(
                    (
                        pre_images[key],
                        file
                    )
                )

    return pairs