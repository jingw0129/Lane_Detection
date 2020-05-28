import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# define the ROI
def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygon = np.array([
        [(0, int(height * 4 / 7)),
         (width, int(height * 4 / 7)), (width, height), (0, height)]

    ])
    mask = np.zeros_like(image)
    #     black mask fill by whites
    #  we have to change from triangle to polygons
    cv2.fillPoly(mask, np.int32([polygon]), 255)
    #   show only the region of image traced by the polygonal contour of the mask
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def Canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest_above_skyline(image):
    height = image.shape[0]
    width = image.shape[1]
    polygon = np.array([
        [(0, int(height * 3 / 7)),
         (width, int(height * 3 / 7)), (width, 0), (0, 0)]

    ])
    mask = np.zeros_like(image)
    #     black mask fill by whites
    #  we have to change from triangle to polygons
    cv2.fillPoly(mask, np.int32([polygon]), 255)
    #   show only the region of image traced by the polygonal contour of the mask
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image