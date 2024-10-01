#!/usr/bin/python
import os
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
import matplotlib.pyplot as plt

def fit_line(c, x):

    if(c < -0.5):
        y = c * x[2,0] + x[3,0]
    elif(-0.5 <= c < 0.5):
        y = (c+0.5)*x[1,0] + c*x[2,0] + x[3,0]
    else:
        y = (c-0.5)*x[0,0] + (c+0.5)*x[1,0] + c*x[2,0] + x[3,0]

    return y


def main():
    
    # Read in data
    data= np.loadtxt('./calibration.txt', dtype=float, delimiter =' ')
    rows = data.shape[0]
    commanded = data[:,0].reshape(rows, 1)
    measured = data[:,1].reshape(rows, 1)

    # Solve Ax = b
    c_nott = np.zeros((rows,1))
    c_nott[commanded[:,0] >= 0.5] = 1
    c_not = np.zeros((rows,1))
    c_not[commanded[:,0] >= -0.5] = 1

    A = np.hstack(((commanded-0.5)*c_nott, (commanded+0.5)*c_not, commanded, np.ones((rows,1))))
    #print(A)
    b = measured
    Ap = np.dot(inv(np.dot(np.transpose(A),A)), np.transpose(A))
    x = np.dot(Ap, b)
    print("least-squares fit parameters: %f, %f, %f, %f" %(x[0,0], x[1,0], x[2,0], x[3,0]))

    # Calculate sum of square error
    errSum = 0
    for i in range(0, rows):
        errSum += (((commanded[i,0]-0.5)*(c_nott[i,0])*x[0,0] +
                    (commanded[i,0]+0.5)*(c_not[i,0])*x[1,0]  +
                    commanded[i,0] * x[2,0] + x[3,0]) - measured[i,0])**2

    print("Sum of squared errors = %f" %errSum)

    # Prediction with piecewise least-squares fit
    print("Prediction of measurement with piecewise least-squares fit for c = 0.68: %f" %(fit_line(0.68, x)))

    # Plot
    fig, ax = plt.subplots()
    data_point = ax.scatter(commanded, measured, marker="x", c="blue", label="Data")
    
    x1, y1 = [-1, -0.5], [fit_line(-1, x), fit_line(-0.5, x)]
    x2, y2 = [-0.5, 0.5], [fit_line(-0.5, x), fit_line(0.5, x)]
    x3, y3 = [0.5, 1], [fit_line(0.5, x), fit_line(1, x)]
    line = ax.plot(x1, y1, x2, y2, x3, y3, c="r", label="m = %f(c-0.5)c_nott + %f(c+0.5)c_not + %f c + %f" %(x[0,0], x[1,0], x[2,0], x[3,0]))
    ax.set_title("Calibration Data")
    ax.set_xlabel("Commanded data (c)")
    ax.set_ylabel("Measured data (m)")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == '__main__':
    main()
