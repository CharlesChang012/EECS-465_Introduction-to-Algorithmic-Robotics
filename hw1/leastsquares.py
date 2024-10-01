#!/usr/bin/python
import os
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
import matplotlib.pyplot as plt

def main():
    
    # Read in data
    data= np.loadtxt('./calibration.txt', dtype=float, delimiter =' ')
    rows = data.shape[0]
    commanded = data[:,0].reshape(rows, 1)
    measured = data[:,1].reshape(rows, 1)

    # Solve Ax = b
    A = np.hstack((commanded, np.ones((rows, 1))))
    b = measured
    Ap = np.dot(inv(np.dot(np.transpose(A),A)), np.transpose(A))
    x = np.dot(Ap, b)
    print("least-squares fit parameters: %f, %f" %(x[0,0], x[1,0]))

    # Calculate sum of square error
    errSum = 0
    for i in range(0, rows):
        errSum += ((commanded[i,0]*x[0,0]+x[1,0])-measured[i,0])**2

    print("Sum of squared errors = %f" %errSum)

    # Plot
    fig, ax = plt.subplots()
    data_point = ax.scatter(commanded, measured, marker="x", c="blue", label="Data")
    
    x1, y1 = [-1, (1-x[1,0])/x[0,0]], [-x[0,0]+x[1,0], 1]
    line = ax.plot(x1, y1, c="r", label="m = %f c + %f" %(x[0,0], x[1,0]))
    ax.set_title("Calibration Data")
    ax.set_xlabel("Commanded data (c)")
    ax.set_ylabel("Measured data (m)")
    plt.legend(loc="lower right")
    plt.show()

if __name__ == '__main__':
    main()
