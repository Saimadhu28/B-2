import cv2
import numpy as np

def crop_building(image, building):

    polygon = building["polygon"]

    xmin, ymin, xmax, ymax = map(int, polygon.bounds)

    xmin = max(0, xmin)
    ymin = max(0, ymin)
    xmax = min(image.shape[1], xmax)
    ymax = min(image.shape[0], ymax)

    crop = image[ymin:ymax, xmin:xmax]

    points = np.array(polygon.exterior.coords)

    points[:,0] -= xmin
    points[:,1] -= ymin

    points = points.astype(np.int32)

    mask = np.zeros(crop.shape[:2], dtype=np.uint8)

    cv2.fillPoly(mask, [points], 255)

    result = cv2.bitwise_and(crop, crop, mask=mask)

    return result