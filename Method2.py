from Make_Lines import make_coordinates
import numpy as np


def k_right_con(k):
    if k > 0.2:
        return True


def k_left_con(k):
    if k < -0.2:
        return True

def grade_kb(points):
    k_b_r = {}
    k_b_l = {}
    points = sorted(points, key=lambda x: x[0])
    for i in range(len(points) - 1):
        for j in range(len(points)):
            if (points[i][0] - points[j][0]) != 0:
                k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                b = points[i][1] - k * points[i][0]
                if k_right_con(k):
                    k_b_r[k, b] = 0
                if k_left_con(k):
                    k_b_l[k, b] = 0
    return k_b_l, k_b_r

def get_final_line(k_b):
    final_kb = []
    keys_ = list(k_b.keys())
    values_ = list(k_b.values())
    for i in range(len(values_) - 1):
        if abs(keys_[i + 1][0] - keys_[i][0]) <= 0.2 and abs(keys_[i + 1][1] - keys_[i][1]) <= 2:
            values_[i]+=1
            values_[i + 1] +=1
        else:
            values_[i]-=1
            values_[i + 1]-=1
    sort_ = sorted(values_)[-1:]
    score_point = list(zip(values_, keys_))

    for s in score_point:
        if s[0] in sort_:
            final_kb.append(list(s[1]))

    return np.array(final_kb)


def potential_line_points(gray):
    index_ = {}
    points_array = []
    left_centre_point = []
    right_centre_point = []
    left_lines = []
    righ_lines = []
    for col in range(0, gray.shape[1] - 1):
        for row in range(300, 700, 30):
            diff_col = int(gray[row][col + 1]) - int(gray[row][col])
            if abs(diff_col) > 8:
                index_[(row, col)] = diff_col
    #     print(index_)
    A = set()

    L = list(index_.keys())
    for i in range(1, len(L)):
        for j in range(len(L) - 1):
            if L[i][0] == L[j][0] and abs(L[i][1] - L[j][1]) in range(10, 70) and index_[L[i]] * index_[L[j]] < 0 and index_[L[i]] + index_[L[j]] in range(-3, 0):
                if L[j] not in A and L[i] not in A:
                    x = (L[j][1] + L[i][1]) / 2
                    y = L[i][0]
                    A.add(L[i])
                    A.add(L[j])

                    if x <= 600:
                        left_centre_point.append([x, y])
                    if x >= 600:
                        right_centre_point.append([x, y])

    kb_left = get_final_line(grade_kb(left_centre_point)[0])
    kb_right = get_final_line(grade_kb(right_centre_point)[1])

    for kl in kb_left:
        m = make_coordinates(gray, kl)
        if m !=[]:
            left_lines.append(m)
    for kr in kb_right:
        m = make_coordinates(gray, kr)
        if m!=[]:
            righ_lines.append(m)

    return left_lines, righ_lines