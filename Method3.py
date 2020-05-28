import ast
from Hog_Extractor import *
from Make_Lines import Display_Lines_sdm
ave = [496, 393, 302, 492, 793, 403, 971, 503]


with open('Rb_collection1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    Rb = list(reader)
R_collection1 = []
b_collection1 = []
for i in range(len(Rb)):
    R_collection1.append(ast.literal_eval(Rb[i][0]))
    b_collection1.append(ast.literal_eval(Rb[i][1]))

def flatten_features_(F_update):
    F_update_flatten = [val for sublist in F_update for val in sublist]
    F_update_flatten = [F_update_flatten[i:i + 256] for i in range(0, len(F_update_flatten), 256)]
    return F_update_flatten


def test_pre_features(flatten, gray_img_array):
    sub_frames = []
    # flatten = flatten[0]
    # print(flatten)
    l_x1, l_y1 = flatten[0], flatten[1]
    # print(l_x1)
    sub1 = gray_img_array[l_y1 - 30:l_y1 + 30, l_x1 - 30:l_x1 + 30]

    l_x2, l_y2 = flatten[2], flatten[3]
    sub2 = gray_img_array[l_y2 - 30:l_y2 + 30, l_x2 - 30:l_x2 + 30]

    r_x1, r_y1 = flatten[4], flatten[5]
    sub3 = gray_img_array[r_y1 - 30:r_y1 + 30, r_x1 - 30:r_x1 + 30]

    r_x2, r_y2 = flatten[6], flatten[7]
    sub4 = gray_img_array[r_y2 - 30:r_y2 + 30, r_x2 - 30:r_x2 + 30]

    sub_frames.append((sub1, sub2, sub3, sub4))

    return sub_frames[0]


def test_Hog_Extractor(flatten_coors_array, frame):
    features = []
    # print 4 sub frames saved in a list, 311 frames are saved in sub_frame
    sub_frames = test_pre_features(flatten_coors_array, frame)

    for i in range(len(sub_frames)):
        hog = Hog_descriptor(sub_frames[i])
        vector, img = hog.extract()

        features.append(vector[0])
    return features


def testing(R_collection, features, B_collection, start,k,frame):
    final_xy_ = []
    final_features = []
    flat_features = flatten_features_(features)

    for f in flat_features:
        test_xy = np.dot(R_collection[k], np.array(f)) + B_collection[k]
        start=np.int_(test_xy+np.array(start))
#         print(start)
        fea = flatten_features_(test_Hog_Extractor(start,frame))
        final_xy_.append(start)
        final_features.append(fea[0])
    return final_xy_, final_features