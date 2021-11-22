import math

import numpy as np
from matplotlib import pyplot as plt
import random
alpha = 10E-2
def ex2_a():
    r1_List = []
    r2_List = []
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
    plt.plot(x, y, 'x',alpha=0.2)
    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    iterations = 10
    d1 = np.array([0,0])
    d2 = np.array([0, 0])
    for i in range(iterations):
        for point in c.T:
                r1Close: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)
                r2Close: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)
                if r1Close < r2Close:
                    d1 = d1 + (point - r1)
                else:
                    d2 = d2 + (point - r2)
        r1 = r1 + (alpha/1000)*d1
        r2 = r2 + (alpha / 1000) * d2
        r1_List.append((r1[0], r1[1]))
        r2_List.append((r2[0], r2[1]))
    r1_List_NPArray_T = np.asarray(r1_List).T
    r2_List_NPArray_T = np.asarray(r2_List).T

    plt.scatter(r1_List_NPArray_T[0], r1_List_NPArray_T[1],label = "r1_list")
    plt.scatter(r2_List_NPArray_T[0], r2_List_NPArray_T[1],label = "r2_list")
    plt.legend()
    plt.axis('equal')
    plt.show()

def ex2_b():
    r1_List = []
    r2_List = []
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
    #plt.plot(x, y, 'x',alpha=0.2)
    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    iterations = 10
    d1 = np.array([0,0])
    d2 = np.array([0, 0])

    closer_r1_cluster_a = []
    closer_r1_cluster_b = []
    closer_r2_cluster_a = []
    closer_r2_cluster_b = []
    a_transposed = a.T
    b_transposed = b.T

    for i in range(iterations):
        for point in c.T:
                r1Close: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)
                r2Close: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)
                if r1Close < r2Close:
                    d1 = d1 + (point - r1)
                else:
                    d2 = d2 + (point - r2)
                if r1Close < r2Close:
                    if point in a_transposed:
                        closer_r1_cluster_a.append(point)
                    elif point in b_transposed:
                        closer_r1_cluster_b.append(point)
                else:
                    if point in a_transposed:
                        closer_r2_cluster_a.append(point)
                    elif point in b_transposed:
                        closer_r2_cluster_b.append(point)
        r1 = r1 + (alpha/1000)*d1
        r2 = r2 + (alpha / 1000) * d2
        r1_List.append((r1[0], r1[1]))
        r2_List.append((r2[0], r2[1]))
    closer_r1_cluster_a_transposed= np.asarray(closer_r1_cluster_a).T
    closer_r1_cluster_b_transposed= np.asarray(closer_r1_cluster_b).T
    closer_r2_cluster_a_transposed= np.asarray(closer_r2_cluster_a).T
    closer_r2_cluster_b_transposed= np.asarray(closer_r2_cluster_b).T

    if closer_r1_cluster_a_transposed.size > 0:
        plt.scatter(closer_r1_cluster_a_transposed[0], closer_r1_cluster_a_transposed[1], label="closer-r1-cluster-a",alpha=0.1)
    if closer_r1_cluster_b_transposed.size>0:
        plt.scatter(closer_r1_cluster_b_transposed[0], closer_r1_cluster_b_transposed[1], label="closer-r1-cluster-b",alpha=0.1)
    if closer_r2_cluster_a_transposed.size>0:
        plt.scatter(closer_r2_cluster_a_transposed[0], closer_r2_cluster_a_transposed[1], label="closer-r2-cluster-a",alpha=0.1)
    if closer_r2_cluster_b_transposed.size>0:
        plt.scatter(closer_r2_cluster_b_transposed[0], closer_r2_cluster_b_transposed[1], label="closer-r2-cluster-b",alpha=0.1)

    plt.scatter(r1[0],r1[1],label="R1")
    plt.scatter(r2[0],r2[1],label="R2")

    plt.legend(loc=2, prop={'size': 6})
    plt.axis('equal')
    #plt.show()

def ex2_c():
    number_of_experiments = 9
    grid: int = int(math.sqrt(number_of_experiments))
    for i in range(number_of_experiments):
        plt.subplot(grid, grid, i + 1)
        ex2_b()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    #ex2_a()
    #ex2_b()
    ex2_c()