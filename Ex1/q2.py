import doctest


def sort_ds(x):
    if type(x) == dict:
        new_dict = {}
        for key in sorted(x):
            new_dict[key] = x.get(key)
        for key, value in new_dict.items():
            new_dict[key] = sort_ds(value)
        x = new_dict
    if type(x) == tuple:
        x = sorted(x)
        for i in range(len(x)):
            x[i] = sort_ds(x[i])
        x = tuple(x)
    if type(x) == list:
        try:
            x.sort()
        except:
            for i in range(len(x)):
                x[i] = sort_ds(x[i])
    return x


def print_sorted(x):
    """
    >>> print_sorted({"a": 5, "c": 6, "b": [1, 4, 3, 2]})
    {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    >>> print_sorted([[4, (4, 5, 3), 3, 2], {"c": 6, "a": 5}, {1: "a", 3: "c", 2: "b"}])
    [[4, (3, 4, 5), 3, 2], {'a': 5, 'c': 6}, {1: 'a', 2: 'b', 3: 'c'}]
    >>> print_sorted([[1, (4, 5, 3), 3, 2], {"c": 5, "a": 6}, {"a":1, "c":3, "b":2}])
    [[1, (3, 4, 5), 3, 2], {'a': 6, 'c': 5}, {'a': 1, 'b': 2, 'c': 3}]
    >>> print_sorted({"a": 5, "c": [1, 4, 3, 2], "b": 6})
    {'a': 5, 'b': 6, 'c': [1, 2, 3, 4]}
    >>> print_sorted({(8,4,9):2, "c": 6, "b": [1, 4, 3, 2]})
    Traceback (most recent call last):
    TypeError: '<' not supported between instances of 'str' and 'tuple'
    """
    print(sort_ds(x))


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    x = {"a": 5, "c": 6, "b": [1, 4, 3, 2]}
    y = [[4, (4, 5, 3), 3, 2], {"c": 6, "a": 5}, {1: "a", 3: "c", 2: "b"}]
    print_sorted(y)
