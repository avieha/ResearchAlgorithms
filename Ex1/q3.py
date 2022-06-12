import doctest

EPS = 0.00001
h = 0.00001


def find_root(f, a, b):
    """
    >>> find_root(f,1,3.5)
    2.000000000694146
    >>> find_root(f,1,9.0)
    2.000005193559831
    >>> find_root(f,3,2.0)
    2.0000000944896588
    >>> find_root(f,4,5.5)
    2.0000023123258606
    >>> find_root(f,1,16)
    2.0000008703340524
    >>> find_root(f,1,30)
    2.000000247472293
    >>> find_root(f,1,2)
    2.0000006981276783
    """
    root = (a + b) / 2
    h = float(f(root) / f_derivative(root))
    while abs(h) >= EPS:
        root = root - h
        h = float(f(root) / f_derivative(root))
    print(root)


def f(x):
    return x ** 2 - 4


def f_derivative(x):
    return float((f(x + h) - f(x)) / h)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    # print(find_root(f, 2, 3))
