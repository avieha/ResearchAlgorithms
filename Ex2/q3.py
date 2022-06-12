import doctest


class List(list):
    """
    mylist = List([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16, 17]]
    ])
        >>> mylist[0]
        [[1, 2], [3, 4]]
        >>> mylist[1]
        [[5, 6], [7, 8]]
        >>> mylist[2]
        [[9, 10], [11, 12]]
        >>> mylist[3]
        [[13, 14], [15, 16, 17]]
        >>> mylist[0]=2
        >>> mylist[0]
        2
        >>> mylist[0,0,0]
        Traceback (most recent call last):
        TypeError: 'int' object is not subscriptable
        >>> mylist[0]=[[1, 2], [3, 4]]
        >>> mylist[0,0,0]
        1
        >>> mylist[0,2]
        Traceback (most recent call last):
        IndexError: tuple index out of range
        >>> mylist[1]="aviem"
        >>> mylist[1]
        'aviem'
        >>> mylist[1][0]
        'a'
        >>> mylist[1]=[[5, 6], [7, 8]]
        >>> mylist[1][0]
        [5, 6]
        >>> mylist[3,1,2]
        17
        >>> mylist[0,0,0]
        1
        >>> mylist[3,3,3]
        Traceback (most recent call last):
        IndexError: list index out of range
        >>> mylist[0,1,0]
        3
        >>> mylist[0,1,0]=-10
        >>> mylist[0,1,0]
        -10
        """

    def __init__(self, list):
        super().__init__(list)

    def __getitem__(self, item):
        if item is None:
            return None
        if isinstance(item, int):
            return super().__getitem__(item)
        elif isinstance(item, tuple):
            row = item[0]
            inner_arr = item[1]
            inner_argument = item[2]
            return self[row][inner_arr][inner_argument]

    def __setitem__(self, key, value):
        if not (isinstance(key, tuple) or isinstance(key, int)):
            raise Exception("wrong value inserted")
        if isinstance(key, int):
            super().__setitem__(key, value)
        if isinstance(key, tuple):
            row = key[0]
            inner_arr = key[1]
            inner_argument = key[2]
            self[row][inner_arr][inner_argument] = value


if __name__ == '__main__':
    mylist = List([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16, 17]]
    ])
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    # print(mylist[0])  # [[1, 2], [3, 4]]
    # print(mylist[0][1])  # [3, 4]
    # print(mylist[0, 0, 0])  # 1
    # print("before change:", mylist[0])  # [[1, 2], [3, 4]]
    # mylist[0] = -4
    # print("after change:", mylist[0])  # 17
