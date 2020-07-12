"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
f) Binary Search
"""


def binary_search(arr_list, first, last, a):
    while first <= last:
        mid = first + (last-first) // 2
        # Check whether a is present at mid or not.
        if arr_list[mid] == a:
            return mid

        elif arr_list[mid] < a:
            first = mid + 1

        else:
            last = mid - 1

    # The element
    # was not present when we reach here.
    return -1


arr_list = [23, 12, 34, 67, 40, 69, 80, 98]
a = int(input("Enter a number to check the existence of element-number in array: "))

# calling the function.
output = binary_search(arr_list, 0, len(arr_list) - 1, a)

if output != -1:
    print("The element exist in the given array list at index", output)
else:
    print("Element does not exist in array list.")
