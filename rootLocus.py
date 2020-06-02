import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math
import sympy


def plt_points():
    ploes_x = [0, -25, -50, -50]
    poles_y = [0, 0, 10, -10]
    plt.scatter(ploes_x, poles_y, s=10, color='red')


def plt_lines_of_asymptotes():
    x = np.linspace(-100, 100, 1000)
    y = 0
    eq1 = x + 31.25
    eq2 = -x - 31.25

    plt.plot(x, eq1, linestyle='--', color='red')
    plt.plot(x, eq2, linestyle='--', color='red')


def curve1_eqn(xr):
    return math.sqrt((xr + 31.25) ** 2 - 22.0996 ** 2)


def plt_second_branch():
    x = np.arange(-9.15, 100, 0.1)
    y = np.arange(-9.15, 100, 0.1)
    i = 0
    for item in x:
        y[i] = curve1_eqn(x[i])
        i = i + 1;

    plt.plot(x, y, color='blue')
    plt.plot(x, -1 * y, color='blue')


def plt_intersect_with_img_axis():
    plt.scatter(0, curve1_eqn(0), s=10, color='red')
    plt.scatter(0, -1 * curve1_eqn(0), s=10, color='red')


def break_away_points(poles, s):
    eqn = sympy.equation(poles, s)
    derivative = sympy.diff(eqn, s)
    diff = sympy.simplify(derivative)
    sol = sympy.solve(diff)
    angle = 0
    angles = []
    points = []
    for j in range(0, len(sol)):
        for i in range(0, len(poles)):
            k = -1 * s
            angle += k
        angles.append(angle)
    for h in range(0, len(angles)):
        if round(angles[h], 1) == -180 or round(angles[h], 1) == 180:
            points.append(sol[h])
    return points[0]


# s = symbol('s')


def plot_first_branch():
    xreal = [0, -25]
    yreal = [0, 0]
    plt.plot(xreal, yreal, color='blue')


def curve2_eqn(xr):
    return math.sqrt((xr + 31.25) ** 2 - 15.8607 ** 2)


def plt_third_branch():
    x = np.arange(-100, -50, 0.1)
    y = np.arange(-100, -50, 0.1)

    i = 0
    for item in x:
        y[i] = curve2_eqn(x[i])
        i = i + 1

    plt.plot(x, y, color='blue')
    plt.plot(x, -1 * y, color='blue')


def wrap_angle(angle):
    if angle >= 180:
        return angle - 360
    else:
        return angle % 360


def get_angle(point1, point2):
    delta_real = point2.real - point1.real
    delta_j = point2.imag - point1.imag
    angle = np.arctan2(delta_j, delta_real)
    return wrap_angle(np.degrees(angle))


def plt_break_away_point():
    break_away_point_x = -9.1504
    break_away_point_y = 0
    plt.scatter(break_away_point_x, break_away_point_y, s=10, color='red')


def Departure_angle(poles, index):
    p = poles[index]
    pole_angles = [get_angle(pole, p) for pole in poles if pole != p]
    return wrap_angle(180 - np.sum(pole_angles))


def get_departure_angles(poles):
    angles = []
    for index in range(len(poles)):
        angles.append(Departure_angle(poles, index))
    return angles


def draw_depature_lines(poles):
    angles = get_departure_angles(poles)
    for i in range(2, len(angles)):
        a = np.tan(angles[i] * np.pi / 180)
        elo = complex(poles[i])
        b = elo.imag - a * elo.real
        xx = np.linspace(-100, -50, 100)
        yy = a * xx + b
        plt.plot(xx, yy, linestyle='-', lw=0.5, color='g')


plt.title("root locus")
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.grid()
draw_depature_lines([0, -25, -50 + 10j, -50 - 10j])
plt_points()


plt_intersect_with_img_axis()
plt_lines_of_asymptotes()
plot_first_branch()
plt_second_branch()
plt_third_branch()
plt_break_away_point()
plt.xlim([-100, 50])
plt.ylim([-60, 60])
plt.show()
