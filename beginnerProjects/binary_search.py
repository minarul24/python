"""
Binary Search Algorithm:
It uses the divide and conquer rule.
The algorithm is for sorted lists.
"""

# binary search method
# a list and a target is passed as the arguments
def binary_search(l, target, low_end = None, high_end = None):

    # midpoint gets the index of the middle of the list
    midpoint = (len(l)) // 2

    # return the index of the middle point if it equals the target
    if l[midpoint] == target:
        return midpoint

    # when target is less than the value at the midpoint of the list
    elif target < l[midpoint]:
        return binary_search(l, target)

    # when target is greater than the value at the midpoint of the list
    else:
        return binary_search(l, target)


sorted_list = [1,2,3,4,5,6,7,8,9]
print(binary_search(sorted_list,6))