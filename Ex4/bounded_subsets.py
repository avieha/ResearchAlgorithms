import doctest
import time
from itertools import chain, combinations


def bounded_subsets(group, c):
    """
    >>> for s in bounded_subsets([1, 2, 3], 4):
    ...     print(s)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    >>> for s in bounded_subsets([1, 2, 3, 4], 1):
    ...     print(s)
    []
    [1]
    >>> for s in bounded_subsets([1, 2, 3, 4], 9): # return all combinations except [1,2,3,4]
    ...     print(s)
    []
    [1]
    [2]
    [3]
    [4]
    [1, 2]
    [1, 3]
    [1, 4]
    [2, 3]
    [2, 4]
    [3, 4]
    [1, 2, 3]
    [1, 2, 4]
    [1, 3, 4]
    [2, 3, 4]
    >>> for s in bounded_subsets([1, 2, 3, 4], 10):  # includes the last one this time
    ...     print(s)
    []
    [1]
    [2]
    [3]
    [4]
    [1, 2]
    [1, 3]
    [1, 4]
    [2, 3]
    [2, 4]
    [3, 4]
    [1, 2, 3]
    [1, 2, 4]
    [1, 3, 4]
    [2, 3, 4]
    [1, 2, 3, 4]
    >>> for s in bounded_subsets([x for x in range(1,20)], 12):
    ...     print(s)
    []
    [1]
    [2]
    [3]
    [4]
    [5]
    [6]
    [7]
    [8]
    [9]
    [10]
    [11]
    [12]
    [1, 2]
    [1, 3]
    [1, 4]
    [1, 5]
    [1, 6]
    [1, 7]
    [1, 8]
    [1, 9]
    [1, 10]
    [1, 11]
    [2, 3]
    [2, 4]
    [2, 5]
    [2, 6]
    [2, 7]
    [2, 8]
    [2, 9]
    [2, 10]
    [3, 4]
    [3, 5]
    [3, 6]
    [3, 7]
    [3, 8]
    [3, 9]
    [4, 5]
    [4, 6]
    [4, 7]
    [4, 8]
    [5, 6]
    [5, 7]
    [1, 2, 3]
    [1, 2, 4]
    [1, 2, 5]
    [1, 2, 6]
    [1, 2, 7]
    [1, 2, 8]
    [1, 2, 9]
    [1, 3, 4]
    [1, 3, 5]
    [1, 3, 6]
    [1, 3, 7]
    [1, 3, 8]
    [1, 4, 5]
    [1, 4, 6]
    [1, 4, 7]
    [1, 5, 6]
    [2, 3, 4]
    [2, 3, 5]
    [2, 3, 6]
    [2, 3, 7]
    [2, 4, 5]
    [2, 4, 6]
    [3, 4, 5]
    [1, 2, 3, 4]
    [1, 2, 3, 5]
    [1, 2, 3, 6]
    [1, 2, 4, 5]
    >>> for s in bounded_subsets([x for x in range(2,20,2)], 10): # combinations of only EVEN NUMBERS
    ...     print(s)
    []
    [2]
    [4]
    [6]
    [8]
    [10]
    [2, 4]
    [2, 6]
    [2, 8]
    [4, 6]
    >>> def take_time():
    ...     start_time = time.time()
    ...     for s in bounded_subsets(range(1,20), 5):
    ...         s
    ...     end_time = time.time()-start_time
    ...     print(end_time<0.3)
    >>> take_time()
    True
    >>> def counter():
    ...     count = 0
    ...     for s in bounded_subsets([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],2):
    ...         count+=1
    ...     print(count)
    >>> counter() # counts the number of different combinations
    121
    """
    List = list(group)
    longest = []
    for i in chain.from_iterable(combinations(List, r) for r in range(len(List) + 1)):
        SubSetSum = 0
        for t in i:
            SubSetSum += t
            if SubSetSum > c:
                break
        if SubSetSum <= c:
            yield list(i)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
