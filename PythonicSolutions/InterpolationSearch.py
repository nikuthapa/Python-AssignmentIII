"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
g) Interpolation Search
"""


# low = starting index in array[],
# high = ending index in array[].
# a = element to searched.
def interpolation_search(arr_list, low, high, a):

    if (low <= high and a >= arr_list[low] and a <= arr_list[high]):
        position = low + ((high - low) // (arr_list[high] - arr_list[low]) * (a - arr_list[low]))
        if arr_list[position] == a:
            return position

        if arr_list[position] < a:
            return interpolation_search(arr_list, position + 1, high, a)

        if arr_list[position] > a:
            return interpolation_search(arr_list, low, position - 1, a)
    return -1


arr_list = [20, 10, 12, 30, 35, 40, 60, 50, 25, 45, 46, 55, 70, 67, 80]
a = int(input("Enter a number to check the existence of element-number in array: "))
index = interpolation_search(arr_list, 0, len(arr_list) - 1, a)

if index != -1:
    print("The element exist in array list at index", index)
else:
    print("The element does not exist in given array list.")

