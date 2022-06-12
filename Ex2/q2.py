import doctest

global_dict = {}


def lastcall(f):
    """
    >>> f1(0)
    0
    >>> f2(0)
    0
    >>> f3(0)
    0
    >>> f1(1)
    1
    >>> f1(0)
    I already told you that the answer is  0 !
    >>> f1(-2)
    -2
    >>> f1("aviem")
    'aviem'
    >>> f1("aviem")
    I already told you that the answer is  aviem !
    >>> f2("aviem")
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    >>> f1(3-2*4)
    -5
    >>> f1(-100)
    -100
    >>> f1(200)
    200
    >>> f1(50-2+3*4)
    60
    >>> f2(2)
    4
    >>> f1(4)
    4
    >>> f1(4)
    I already told you that the answer is  4 !
    >>> f2(f1(4))  # the answer is 16, but f1(4) was already calculated!
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    >>> f3(3-2*4)
    -125
    >>> f3(-100)
    -1000000
    >>> f3(f3(3-2*4))
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    >>> f1(f2(f3(3)))
    729
    """

    def wrapper(*args):
        output = f(*args)
        name = str(f.__name__)
        if name in global_dict:
            if output in global_dict[name]:
                print("I already told you that the answer is ", output, "!")
            else:
                global_dict[name].append(output)
                return output
        else:
            global_dict[name] = []
            global_dict[name].append(output)
            return output

    return wrapper


@lastcall
def f1(x):
    return x


@lastcall
def f2(x: int):
    return x ** 2


@lastcall
def f3(x: int):
    return x ** 3


if __name__ == '__main__':
    list = [1, 2, 3, 2, 1, 4, 1, 5, -1]
    # for x in list:
    #     print(f1(x))
    # for x in list:
    #     print(f2(x))
    # for x in list:
    #     print(f3(x))
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
