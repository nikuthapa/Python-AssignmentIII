"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
e) Linear Search
"""


def linear_search(arr_list, length, a):
    for i in range(0, length):
        if arr_list[i] == a:
            return i
    return -1


arr_list = [1, 2, 3, 5, 7, 9, 11, 12, 14]
a = int(input("Enter a number to check the existence of element-number in array: "))
length = len(arr_list)
output = linear_search(arr_list, length, a)

if output == -1:
    print("Element does not exist in the array list.")
else:
    print("Element exist in the array list at index", output)

