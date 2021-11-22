import math
import random

import numpy as np
from matplotlib import pyplot as plt

alpha = 10E-1
def average_point(a,b):
    average_x = (a[0]+b[0])/2
    average_y = (a[1]+b[1])/2
    return np.asarray([average_x, average_y])

def distance_between_points(a,b):
    return math.dist( (a[0],a[1]) , (b[0],b[1]) )
def closest_two_points(list_points):

    minimum_point1 = list_points[0]
    minimum_point2 = list_points[1]
    minimum_distance = distance_between_points(minimum_point1,minimum_point2)
    for i in list_points:
        for j in list_points:
            if not i[0]== j[0] and i[1]== j[1]:
                distance = distance_between_points(i,j)
                if distance < minimum_distance:
                    minimum_point1 = i
                    minimum_point2 = j
                    minimum_distance = distance

    return minimum_point1,minimum_point2

def ex_3():
    r1_List = []
    r2_List = []
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 200).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 200).T
    c = np.concatenate((a, b), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    x = c[0]
    y = c[1]
    plt.plot(x, y, 'x',alpha=0.7)

    points_list = c.T
    average_pnt = average_point(points_list[0],points_list[1])
    while len(points_list) > 2:
        closest_point1, closest_point2 = closest_two_points(points_list)
        average_pnt = average_point(closest_point1,closest_point2)
        points_list = np.delete(points_list,np.where(points_list==closest_point1),axis=0)
        points_list = np.delete(points_list, np.where(points_list == closest_point2),axis=0)
        points_list = np.append(points_list,[average_pnt],axis=0)
        print(len(points_list))

    plt.axis('equal')
    plt.scatter(points_list[0][0],points_list[0][1],label="R1",alpha=1)
    plt.scatter(points_list[1][0], points_list[1][1], label="R2", alpha=1)
    plt.legend()
    plt.show()



if __name__ == '__main__':
    ex_3()