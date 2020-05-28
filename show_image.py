
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

path = "//192.168.199.148/Videos/wheeldone2018-2-10Video(Company-HJ)-conbine/2018-2-10.avi"

cap = cv2.VideoCapture(path)
success = True
c = 1
timeF = 100

while (success):
    success, frame = cap.read()
    if np.any(frame) is not None:
        if c % timeF == 0:
            lane_image = np.copy(frame)
            H = lane_image.shape[0]
            W = lane_image.shape[1]
            for j in range(0, int(H/3), 60):
                for i in range(0, 1261, 60):
                    name = str([j, j + 60, i,i + 60])
                    cropped = lane_image[j:j + 60, i:i + 60]
                    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite('//192.168.199.148/ml/LaneSample/NEG3/' + str(name) + str(c) + ".png", gray)


            cv2.imshow("video", lane_image)
            key = cv2.waitKey(20)
            if key == 25:
                break
        c += 1
cap.release()
cv2.destroyAllWindows()


# from image_preprocessing import *
# from Make_Lines import *
# from Match import match_method1_3
# from weighted_line_chart import *
# from Method2 import *
# import numpy as np
# from Method3 import *
#
# left_weight_line_list = {}
# right_weight_line_list = {}
# path = "C:/Users/win10-zw/Desktop/myFile/20180128_102033_B.ts"
#
# cap = cv2.VideoCapture(path)
# success = True
# c = 1
# timeF = 1
#
#
# demo = []
#
# while (success):
#     success, frame = cap.read()
#     if np.any(frame) is not None:
#         if c % timeF == 0:
#             lane_image = np.copy(frame)
#             canny = Canny(lane_image)
#             cropped_img = region_of_interest(canny)
#
#             gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
#             M2_blur = cv2.GaussianBlur(gray, (5, 5), 0)
#
#             # method3 SDM
#             testing_features = test_Hog_Extractor(ave,gray)
#             test_result = testing(R_collection1, testing_features, b_collection1, ave, 0, gray)
#             # print(test_result[0])
#             test_result1 = testing(R_collection1, test_result[1], b_collection1, test_result[0][0], 1, gray)
#             # print(test_result1[0])
#             test_result2 = testing(R_collection1, test_result1[1], b_collection1, test_result1[0][0], 2, gray)
#             # print(test_result2[0])
#             test_result3 = testing(R_collection1, test_result2[1], b_collection1, test_result2[0][0], 3, gray)
#             # print(test_result3[0])
#             test_result4 = testing(R_collection1, test_result3[1], b_collection1, test_result3[0][0], 4, gray)
#             # print(test_result4[0])
#             test_result5 = testing(R_collection1, test_result4[1], b_collection1, test_result4[0][0], 5, gray)
#             # print(test_result5[0])
#             # test_result6 = testing(R_collection1, test_result5[1], b_collection1, test_result5[0][0], 6, gray)
#             # print(test_result6[0])
#             # test_result7 = testing(R_collection, test_result6[1], B_collection, test_result6[0], 7)
#             # xy_collection_predict = []
#             # for i in range(6):
#             #     t = testing(R_collection1, testing_features, b_collection1, i, gray)
#             #     xy_collection_predict.append(t[0])
#             sdm_display_lines = test_result5[0]
#             sdm_line_left = Display_Lines_sdm(lane_image, sdm_display_lines)[0]
#             sdm_line_right = Display_Lines_sdm(lane_image, sdm_display_lines)[1]
#             # print(sdm_line_left)
#
#             # HoughTransform
#             lines_hough = cv2.HoughLinesP(cropped_img, 1, np.pi / 180, 80, np.array([]), minLineLength=60, maxLineGap=10)
#             method1_lines_left = average_slope_intersect(lane_image, lines_hough)[0]
#             method1_lines_right = average_slope_intersect(lane_image, lines_hough)[1]
#
#             #  # 上升下降沿
#             method2_lines_left = potential_line_points(M2_blur)[0]
#             method2_lines_right = potential_line_points(M2_blur)[1]
#
#
#             # match three methods
#             left_lines = match_method1_3(method1_lines_left, method2_lines_left,sdm_line_left, 0.2, 2)
#             right_lines = match_method1_3(method1_lines_right, method2_lines_right,sdm_line_right, 0.2, 2)
#             #update weight lists
#             left_weight_line_list = update_weight_list(left_lines, left_weight_line_list, -20, 0.3,100)
#             right_weight_line_list = update_weight_list(right_lines, right_weight_line_list, -20, 0.3, 100)
#
#             # define output lines
#             display_lines_left = output_line(left_weight_line_list)
#             display_lines_right = output_line(right_weight_line_list)
#             # print(display_lines_left)
#             # print(display_lines_right)
#
#             display_lines = list(display_lines_left) + list(display_lines_right)
#             # show image
#             display_line_image = Display_Lines(lane_image, display_lines)
#             combo_image = cv2.addWeighted(lane_image, 0.8, display_line_image, 1, 1)
#             demo.append(combo_image)
#             cv2.imshow("video", combo_image)
#
#             key = cv2.waitKey(20)
#             if key == 25:
#                 break
#         c += 1
# cap.release()
# cv2.destroyAllWindows()
#
# # Write frames into videos
# pathOut = 'Demo1.avi'
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