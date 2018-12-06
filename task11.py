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
        if is_can_sort(array, array_sort):
            break

    return array


def is_can_sort(array, array_sort):
    return (compare_array(swap_head, array, array_sort) or
            compare_array(swap_tail, array, array_sort))


def compare_array(func, array, array_sort):
    func(array)
    if array == array_sort:
        return True
    else:
        func(array)
    return False


def swap_head(array):
    array[0], array[1] = array[1], array[0]


def swap_tail(array):
    array[-2], array[-1] = array[-1], array[-2]


def shift_left(array):
    # d = deque(array)
    # d.rotate(len(array) - 1)
    # return list(d)
    return array[-(len(array) - 1):] + array[:-(len(array) - 1)]


def generate_random_array(n):
    if n > 4:
        array = [i for i in range(1, n+1)]
        shuffle(array)
        print(array)
        return array


print(hack(generate_random_array(7)))
