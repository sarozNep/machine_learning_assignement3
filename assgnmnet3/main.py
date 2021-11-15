import numpy as np
from matplotlib import pyplot as plt
import random
alpha = 10E-5
def point_generation():
    r1_List_start = []
    r2_List_start = []
    r1_List_final = []
    r1_List_final = []
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 500).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 500).T
    c = np.concatenate((a, b), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    x = c[0]
    y = c[1]
    plt.plot(x, y, 'x')
    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    iterations = 10
    for i in range(iterations):
        for point in c.T:
            r1Close: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)
            r2Close: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)
            if r1Close < r2Close:
                r1 = (1 - alpha) * r1 + alpha * point
            else:
                r2 = (1 - alpha) * r2 + alpha * point
            if i == 0:
                r1_List_start.append((r1[0], r1[1]))
                r2_List_start.append((r2[0], r2[1]))
            r1_List_final.append((r1[0], r1[1]))
            r1_List_final.append((r2[0], r2[1]))
    r1_List_start_NPArray_T = np.asarray(r1_List_start).T
    r2_List_start_NPArray_T = np.asarray(r2_List_start).T

    r1_List_final_NPArray_T = np.asarray(r1_List_start).T
    r1_List_final_NPArray_T = np.asarray(r2_List_start).T

    plt.scatter(r1_List_start_NPArray_T[0], r1_List_start_NPArray_T[1])
    plt.scatter(r2_List_start_NPArray_T[0], r2_List_start_NPArray_T[1])

    plt.scatter(r1_List_final_NPArray_T[0], r1_List_final_NPArray_T[1])
    plt.scatter(r1_List_final_NPArray_T[0], r1_List_final_NPArray_T[1])
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    point_generation()