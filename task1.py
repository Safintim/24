from random import randint


def length_is_odd(length):
    return length % 2 != 0


def generate_random_array(length_array):
    array = set()
    while len(array) != length_array:
        array.add(randint(0, 255))
    return list(array)


def converter_array_to_start_impulse(array):
    if length_is_odd(len(array)):
        array.sort()
        right_part_array = array[len(array) // 2:]
        right_part_array.reverse()
        array[len(array) // 2:] = right_part_array
        return array
    else:
        return None
