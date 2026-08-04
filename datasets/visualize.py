import cv2

def draw_boxes(image, buildings):

    img = image.copy()

    for b in buildings:

        xmin, ymin, xmax, ymax = map(int, b["bounds"])

        cv2.rectangle(
            img,
            (xmin, ymin),
            (xmax, ymax),
            (0,255,0),
            1
        )

    return img