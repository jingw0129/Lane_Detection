import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def average_slope_intersect(image, lines):
    left_fit = []
    right_fit = []
    right_line = []
    left_line = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0].reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]
            if slope < -0.3 and 0 < x2 < 600:
                left_fit.append((slope, intercept))
            elif slope > 0.3 and x2 > 600:
                right_fit.append((slope, intercept))

    for lf in left_fit:
        m = make_coordinates(image, lf)
        if m!=[]:
            left_line.append(m)

    for rf in right_fit:
        m  = make_coordinates(image, rf)
        if m !=[]:
            right_line.append(m)

    return np.array(left_line), np.array(right_line)


def make_coordinates(image, line_parameters):
    lines = []
    if line_parameters is not None:
        try:
            slope, intercept = line_parameters
            y1 = int(image.shape[0])  # <-- The bottom of the image
            y2 = int(3.5 * image.shape[0] / 7)  # <-- Just below the horizon
            x1 = int((y1 - intercept) / slope)
            x2 = int((y2 - intercept) / slope)
            if x2> 350:
                lines.append([x1, y1, x2, y2])

        except:
            print("line_parametersnot found")

    return lines


def Display_Lines(image, lines):
    line_image = np.zeros_like(image)
    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)
    except:
        print('None')
    return line_image


def make_lines(line_parameters,image):
    x1=0
    y1=0
    x2=0
    y2=0
    if line_parameters is not None:
        try:
            slope, intercept = line_parameters
            y1 = int(image.shape[0])  # <-- The bottom of the image
            y2 = int(3.5 * image.shape[0] / 7)  # <-- Just below the horizon
            x1 = int((y1 - intercept) / slope)
            x2 = int((y2 - intercept) / slope)
        except:
            print("line_parametersnot found")
    return x1,y1,x2,y2


def Display_Lines_sdm(image, lines):
    line_image = np.zeros_like(image)
    left_lines = []
    right_lines = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2, x3, y3, x4, y4 = line.reshape(8)
            line_parameters1 = (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1
            line_parameters2 = (y4 - y3) / (x4 - x3), y3 - ((y4 - y3) / (x4 - x3)) * x3
            line1 = make_lines(line_parameters1,image)
            line2 = make_lines(line_parameters2,image)
            cv2.line(line_image, (line1[0], line1[1]), (line1[2], line1[3]), (97, 222, 44), 5)
            cv2.line(line_image, (line2[0], line2[1]), (line2[2], line2[3]), (97, 222, 44), 5)
            left_lines = [line1[0], line1[1], line1[2], line1[3]]
            right_lines = [line2[0], line2[1], line2[2], line2[3]]
    return np.array([left_lines]), np.array([right_lines]), line_image