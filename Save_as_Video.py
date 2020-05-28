# import glob
# from os.path import isfile, join
# import os.path as ops
# from show_image import demo
# import cv2
#
#
# pathOut = 'Demo3.avi'
# # frame per second. read fps images each second
# fps = 20
# height, width, layers = demo[0].shape
# size = (width,height)
# out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
#
# for i in range(len(demo)):
#     # writing to a image array
#     out.write(demo[i])
# out.release()

from image_preprocessing import *
from Make_Lines import *
from Match import match_method1_3
from weighted_line_chart import *
from Method2 import *
import numpy as np
from Method3 import *

path = "//192.168.199.148/Videos/20180706Video(Company)_conbine/20180706.avi"

cap = cv2.VideoCapture(path)
success = True
c = 1
timeF = 50

while (success):
    success, frame = cap.read()
    if np.any(frame) is not None:
        if c % timeF == 0:
            lane_image = np.copy(frame)
            canny = Canny(lane_image)
            cropped_img = region_of_interest(canny)

            # HoughTransform
            lines_hough = cv2.HoughLinesP(cropped_img, 1, np.pi / 180, 80, np.array([]), minLineLength=60, maxLineGap=10)
            print(lines_hough)
            try:
                for lines in lines_hough:
                    if abs(lines[0][1]-lines[0][3]) > 50 and abs(lines[0][0]-lines[0][2]) > 50:
                        cropped = lane_image[lines[0][1]: lines[0][3], lines[0][0]: lines[0][2]]
                        gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                        cv2.imwrite("//192.168.199.148/ml/LaneSample/lane_cropped_sample11/" + str(lines[0]) + ".png", gray)
            except:
                print('NoneType')
            display_line_image = Display_Lines(lane_image, lines_hough)
            combo_image = cv2.addWeighted(lane_image, 0.8, display_line_image, 1, 1)
            # demo.append(combo_image)
            cv2.imshow("video", combo_image)
            key = cv2.waitKey(20)
            if key == 25:
                break
        c += 1
cap.release()
cv2.destroyAllWindows()
