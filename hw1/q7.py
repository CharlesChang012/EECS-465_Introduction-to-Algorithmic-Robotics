#!/usr/bin/python
import os
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

def rot_z(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],  # np.cos reads in angles in radians
                     [np.sin(theta), np.cos(theta), 0], 
                     [0, 0, 1]])

def rot_y(theta):
    return np.array([[np.cos(theta), 0, np.sin(theta)], 
                     [0, 1, 0], 
                     [-np.sin(theta), 0, np.cos(theta)]])

def main():
    R = np.dot(rot_z(np.pi/2), rot_y(-np.pi/5))
    R = np.dot(R, rot_z(np.pi))
    print("R =\n", np.round(R, 3))  


if __name__ == '__main__':
    main()
