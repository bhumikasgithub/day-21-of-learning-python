#1
def filter_list(lst):
    return [item for item in lst if type(item) == int]

# Example user input
input_list = [1, "hello", 42, "world", 7]

# Call the function and print result
print("Filtered integers:", filter_list(input_list))

#2
def add_indexes(lst):
    return [num + index for index, num in enumerate(lst)]

# Example test cases
print(add_indexes([0, 0, 0, 0, 0]))      # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))      # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))      # ➞ [5, 5, 5, 5, 5]

#3

import math  # We need this for math.pi

def cone_volume(height, radius):
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 2)

# Test cases
print(cone_volume(3, 2))    # ➞ 12.57
print(cone_volume(15, 6))   # ➞ 565.49
print(cone_volume(18, 0))   # ➞ 0.0

#4
def triangle(n):
    return n * (n + 1) // 2

# Test cases
print(triangle(1))     # ➞ 1
print(triangle(6))     # ➞ 21
print(triangle(215))   # ➞ 23220

#5
def missing_num(lst):
    return 55 - sum(lst)

# Test cases
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # ➞ 5
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))   # ➞ 10
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))  # ➞ 7


