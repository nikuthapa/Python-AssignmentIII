"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
i) Tower of Hanoi problem for ‘n’ number of disks.
"""


def tower_of_hanoi(x, from_rod, to_rod, aux_rod):
    if x == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(x - 1, from_rod, aux_rod, to_rod)
    print("Move disk", x, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(x - 1, aux_rod, to_rod, from_rod)


x = int(input("Enter an input number:"))
print("Output:")
tower_of_hanoi(x, 'X', 'Z', 'Y')