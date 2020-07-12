"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
b) Insertion Sort
"""


def insertion_sort(list_b):
     for i in range(1, len(list_b)):
        latest_value = list_b[i]
        location = i

        while location > 0 and list_b[location-1] > latest_value:
            list_b[location] = list_b[location-1]
            location = location-1

        list_b[location] = latest_value


list_b = [9, 3, 4, 1, 6, 2, 7, 15, 23, 14]
insertion_sort(list_b)

print("Sorted list:\n", list_b)