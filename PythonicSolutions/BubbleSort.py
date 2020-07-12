"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
a) Bubble Sort
"""


def bubble_sort(list_a):
    for number in range(len(list_a)-1, 0, -1):
        for i in range(number):
            if list_a[i] > list_a[i+1]:
                temporary1 = list_a[i]
                list_a[i] = list_a[i+1]
                list_a[i+1] = temporary1


list_a = [20, 11, 34, 25, 56, 79, 30, 55, 12]
bubble_sort(list_a)

print("Sorted list:\n", list_a)