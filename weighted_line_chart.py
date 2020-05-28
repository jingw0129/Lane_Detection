import numpy as np

# left_weight_line_list = {}
# right_weight_line_list = {}

def update_weight_list(method, weight_dic, thre, diff_k, diff_x):
    # print(method)
    new_lines = []

    if len(weight_dic) == 0:
        for m in method:
            line = m[0]
            weight_dic[tuple(line)] = [0, 0]
    if len(method) != 0:
        # print(method)
        a = 0
        weight_dic_copy = dict(weight_dic)
        # k_diff = 0
        for k, v in weight_dic_copy.items():
            for m in method:
                line = m[0]

                x0_diff = abs(line[0] - k[0])
                x2_diff = abs(line[2] - k[2])

                if line[2] - line[0]!=0 and k[2] - k[0] !=0:
                    k_diff = abs((line[3] - line[1]) / (line[2] - line[0]) - (k[3] - k[1]) / (k[2] - k[0]))

                    # break the process if match up
                    if x0_diff <= diff_x and k_diff <= diff_k and v[1] != 1:
                        weight_dic[k][0] += 1
                        weight_dic[k][1] = 1
                        # print(k)
                        weight_dic[tuple(line)] = weight_dic.pop(k)

                        a += 1
                    else:
                        if v[1] != 1:
                            weight_dic[k][0] -= 1
                            weight_dic[k][1] = 1
                            new_lines.append(tuple(line))
        for k in weight_dic.keys():
            weight_dic[k][1] = 0

        if a == 0:
            for n in new_lines:
                weight_dic[n] = [0, 0]

    delete_KV_dic(weight_dic, thre)
    # print(weight_dic)
    return weight_dic


def output_line(weight_line_list):
    output_lines = []
    for k, v in weight_line_list.items():
        if v[0] >= 3:
            output_lines.append([list(k)])

    # print(np.array(output_lines))
    return np.array(output_lines)


# seperate left line and right line inorder to save in weight line list.
# left lines are rarely detected by method either 1 or 2 so we define the different threshold.

def delete_KV_dic(dic, thre):
    if dic is not None:
        # Create a temporary copy of dictionary
        copyOfDict = dict(dic)
        # Iterate over the temporary dictionary and delete corresponding key from original dictionary
        for (key, value) in copyOfDict.items():
            if value[0] <= thre or value[0] > 100:
                del dic[key]
    return dic
