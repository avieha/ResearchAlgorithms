import doctest
import inspect


def f(x, y: int, z: float):
    return x + y + z


def safe_call(f, *item_names):
    """
        >>> safe_call(f,1,3,3.5)
        7.5
        >>> safe_call(f,1,3,9.0)
        13.0
        >>> safe_call(f,1,3,2.0)
        6.0
        >>> safe_call(f,1-3,3,3.5)
        4.5
        >>> safe_call(f,1,"a",3.5)
        Traceback (most recent call last):
        Exception: Wrong type of argument
        """
    temp = inspect.getfullargspec(f)
    args = temp.args
    f_types = []
    for j in range(len(args)):
        if temp.annotations.__contains__(args[j]):
            f_types.append(temp.annotations.get(args[j]))
        else:
            f_types.append("")
    i = 0
    for argument in item_names:
        if f_types[i] != '':
            if type(argument) != f_types[i]:
                raise Exception("Wrong type of argument")
                continue
        if i == len(f_types) - 1:
            break
        i += 1
    print(f(*item_names))


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    # safe_call(f, "a", 3, 3.5)
