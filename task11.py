from random import shuffle, randint
from collections import deque


def hack(array, count=3):
    array_sort = sorted(array)
    while array != array_sort:
        start_index = randint(0, len(array) - count)
        part_array = array[start_index:start_index + count]
        max_part_array = max(part_array)

        for i in range(len(part_array)):
            if max_part_array == part_array[len(part_array)-1]:
                break
            part_array = shift_left(part_array)

        array[start_index:start_index + count] = part_array
        print(array)
    return array


def shift_left(array):
    # d = deque(array)
    # d.rotate(len(array) - 1)
    # return list(d)
    return array[-(len(array) - 1):] + array[:-(len(array) - 1)]


def generate_random_array(n):
    if n > 4:
        array = [i for i in range(1, n+1)]
        shuffle(array)
        # print(array)
        return array


hack(generate_random_array(7))