"""
Make pythonic solutions for each of the following data structure
and algorithm problems.
c) Quick Sort
"""


def quick_sort(list_c):
    quick_sort_aid(list_c, 0, len(list_c)-1)


def quick_sort_aid(list_c, f_item, l_item):   # f_item stands for first element and l_item stands for last element.
    if f_item < l_item:
        breaking_point = splitting(list_c, f_item, l_item)
        quick_sort_aid(list_c, f_item,breaking_point-1)
        quick_sort_aid(list_c, breaking_point+1,l_item)


def splitting(list_c, f_item, l_item):
    axis_value = list_c[f_item]
    left_pointer = f_item+1
    right_pointer = l_item

    done = False
    while not done:

        while left_pointer <= right_pointer and list_c[left_pointer] <= axis_value:
            left_pointer += 1

        while list_c[right_pointer] >= axis_value and right_pointer >= left_pointer:
            right_pointer -= 1

        if right_pointer < left_pointer:
            done = True
        else:
            interim = list_c[left_pointer]
            list_c[left_pointer] = list_c[right_pointer]
            list_c[right_pointer] = interim

    interim = list_c[f_item]
    list_c[f_item] = list_c[right_pointer]
    list_c[right_pointer] = interim

    return right_pointer


list_c = [23, 34, 56, 22, 13, 54, 65, 17, 23, 60]
quick_sort(list_c)
print("Sorted list:", list_c)