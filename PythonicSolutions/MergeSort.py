"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
d) Merge Sort
"""


def merge_sort(arr_list):
    print("Splitting array list:", arr_list)
    if len(arr_list) > 1:
        mid = len(arr_list)//2  # finding mid value of array.
        l_half_part = arr_list[:mid]  # division of the array elements
        r_half_part = arr_list[mid:]   # into 2 halves.

        merge_sort(l_half_part)  # sorting first half part.
        merge_sort(r_half_part)  # sporting second half part.

        i = j = k = 0
        while i < len(l_half_part) and j < len(r_half_part):
            if l_half_part[i] < r_half_part[j]:
                arr_list[k] = l_half_part[i]
                i += 1
            else:
                arr_list[k] = r_half_part[j]
                j += 1
            k += 1

        while i < len(l_half_part):
            arr_list[k] = l_half_part[i]
            i += 1
            k += 1

        while j < len(r_half_part):
            arr_list[k] = r_half_part[j]
            j += 1
            k += 1
    print("Merging array list:", arr_list)


arr_list = [3, 1, 6, 2, 7, 3, 23, 17, 25, 35, 28, 15]
print("Given array list:", arr_list)

merge_sort(arr_list)
print("Sorted array list:\n", arr_list)