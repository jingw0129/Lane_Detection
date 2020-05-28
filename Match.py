import numpy as np

def match_method1_3(method1_lines, method2_lines, method3_lines, diff_k, diff_x):
    lines = []
    # k_diff = 0
    m3 = method3_lines[0]
    # print(np.array(m3)*0.2)
    for m1 in method1_lines:
        for m2 in method2_lines:
            # print(method3_lines[0])
            x0_diff = abs(m1[0][0] - m2[0][0])
            x1_diff = abs(m1[0][2] - m2[0][2])
            if m1[0][2] - m1[0][0]!=0 and m2[0][2] - m2[0][0] !=0:
                k_diff = abs((m1[0][3] - m1[0][1]) / (m1[0][2] - m1[0][0]) - (m2[0][3] - m2[0][1]) / (m2[0][2] - m2[0][0]))

                if k_diff<=diff_k and x0_diff <= diff_x:
                    m_ = np.array(m1[0]) * 0.5 + np.array(m2[0]) * 0.3 + np.array(m3)*0.2
                    m_ = [int(e) for e in m_]
                    # print(m_,m3)
                    lines.append([m_])
            if m1[0] is None:
                m_ = np.array(m2[0]) * 0.5 + np.array(m3) * 0.5
                m_ = [int(e) for e in m_]
                lines.append([m_])
            if m2[0] is None:
                m_ = np.array(m1[0]) * 0.7 + np.array(m3) * 0.3
                m_ = [int(e) for e in m_]

                lines.append([m_])
            if m1[0] is None and m2[0] is None:
                # print(m3)
                lines.append([m3])
    return lines
