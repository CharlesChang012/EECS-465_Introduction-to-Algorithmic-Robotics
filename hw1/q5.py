#!/usr/bin/python
import os
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
from numpy.linalg import matrix_rank

def solve(A, b):
    if(det(A) == 0):
        Augmented = np.hstack((A, b.reshape(-1,1)))
        rank_A = matrix_rank(A)
        rank_augmented = matrix_rank(Augmented)
        if(rank_A < rank_augmented):
            print("Rank A is smaller than rank augmented, thus have no solution")
        else:
            print("A is not invertible and rank A is equal to rank augmented, thus have infinite numbers of solutions")
    else:
        x = np.dot(inv(A), b)
        print(x)


def main():
    while(True):
        print("Enter question number: a, b or c")
        qNum = input()
        
        if(qNum == 'a'):
            A = np.array([[0, 0, -1], [4, 1, 1], [-2, 2, 1]])
            b = np.array([3, 1, 1])
            solve(A, b)
        elif(qNum == 'b'):
            A = np.array([[0, -2, 6], [-4, -2, -2], [2, 1, 1]])
            b = np.array([1, -2, 0])
            solve(A, b)
        elif(qNum == 'c'):
            A = np.array([[2, -2], [-4, 3]])
            b = np.array([[3],[-2]])
            solve(A, b)
        else:
            print("Please enter a, b or c in lower case")           


if __name__ == '__main__':
    main()
