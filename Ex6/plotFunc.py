import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import warnings

warnings.filterwarnings('ignore', 'The iteration is not making good progress')


def plotIntersection(x_values, f, g):
    """
        :param x_values: the x values got from the user, by choosing a range
        :param f: the first function
        :param g: the second function
        :return: shows a graph with the two functions and the intersection points
    """
    points = set()
    inter_func = lambda x: f(x) - g(x)
    for i in x_values:
        temp = scipy.optimize.fsolve(inter_func, i)
        xTemp = temp[0]
        fTemp = "%.6f" % f(xTemp)
        gTemp = "%.6f" % g(xTemp)
        if x_values[0] <= xTemp <= x_values[-1]:
            if fTemp == gTemp:  # if their value is equal
                points.add(xTemp)
    # drawing the functions f and g
    plt.plot(x_values, f(x_values))
    plt.plot(x_values, g(x_values))
    # drawing the intersection points
    for point in points:
        plt.plot(point, f(point), 'ro', zorder=3)
    plt.title("Functions f and g")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    f = lambda x: 0.2 * x
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: x ** 2
    g = lambda x: x + 10
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: 0.1 * x
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: 0 * x
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-50, 50, 1000), f, g)
    f = lambda x: 0.2 * x
    g = lambda x: np.cos(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: np.cos(x)
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: x
    g = lambda x: x
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: x ** 3
    g = lambda x: x ** 2 - 2 * x + 10
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: x ** 2 + 2 * x
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: x ** 2 + 2 * x + 4
    g = lambda x: x ** 2 - 2 * x + 2
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
    f = lambda x: np.sin(x)
    g = lambda x: x ** 2 - 2 * x + 2
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
