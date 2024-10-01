#!/usr/bin/python
import os
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

def main():
    while(True):
        print("Enter question number: a, b, c, d, e, f or g");
        qNum = input()
        
        A = np.array([[1, 2], [3, -1]])
        B = np.array([[-2, -2], [4, -3]])

        if(qNum == 'a'):
            print("A+2B =\n", A + 2*B)

        elif(qNum == 'b'):
            print("AB =\n", np.dot(A, B))
            print("BA =\n", np.dot(B, A))

        elif(qNum == 'c'):
            print("A^T =\n", np.transpose(A))

        elif(qNum == 'd'):
            print("B^2 =\n", np.dot(B, B))
        
        elif(qNum == 'e'):
            print("A^T B^T =\n", np.dot(np.transpose(A), np.transpose(B)))
            print("(AB)^T =\n", np.transpose(np.dot(A, B)))

        elif(qNum == 'f'):
            print("det(A) =\n", round(det(A), 3))

        elif(qNum == 'g'):
            print("inv(B) =\n", np.round(inv(B), 3))

        else:
            print("Please enter a, b, c, d, e, f or g in lower case")           


if __name__ == '__main__':
    main()
