"""
Binary Search Algorithm:
It uses the divide and conquer rule.
The algorithm is for sorted lists.
"""


# binary search method
# a list and a target is passed as the arguments


def binary_search(l, target, low_end = None, high_end = None):

    # when low_end is not provided it assumes it to be the starting of the list
    if low_end is None:
        low_end = 0
    # when high_end is not provided then it assumes it to be the end of the list
    if high_end is None:
        high_end = len(l) -1

    # high_end can never be the lower than low_end theoretically but it could be if it is not  in the list
    # so it will return -1
    if high_end < low_end:
        return -1

    # midpoint gets the index of the middle of the list
    midpoint = (low_end + high_end) // 2

    # return the index of the middle point if it equals the target
    if l[midpoint] == target:
        return midpoint

    # when target is less than the value at the midpoint of the list
    elif target < l[midpoint]:
        # recursion
        # low_end remains the same but high end becomes the left of midpoint of the original list as per divide rule
        return binary_search(l, target, low_end, midpoint-1)

    # when target is greater than the value at the midpoint of the list
    else:
        # high end remains the same
        # the new low end is the right of the midpoint of the original list
        return binary_search(l, target, midpoint+1, high_end)
