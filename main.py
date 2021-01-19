# Lets create a binary search algorithm
import numpy as np

my_array= np.random.randint(1,101,20)

print(my_array)

guessed_number = input('Please guess a number between 0 and 100')

for x in range(0, 6):
    length = len(my_array)
    middle_index = length // 2
    first_half = my_array[:middle_index]
    second_half = my_array[middle_index:]
    print(first_half)
    print(second_half)
    if guessed_number in first_half:
        my_array = first_half
        length = len(my_array)
        middle_index = length // 2
        first_half = my_array[:middle_index]
        second_half = my_array[middle_index:]
        print(first_half)
        print(second_half)
    if guessed_number not in first_half:
        my_array = second_half
        length = len(my_array)
        middle_index = length // 2
        first_half = my_array[:middle_index]
        second_half = my_array[middle_index:]
        print(first_half)
        print(second_half)



