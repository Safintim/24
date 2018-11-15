from random import randint


def length_is_odd(length):
    return length % 2 != 0


def generate_random_array(length_array):
    array = set()
    while len(array) != length_array:
        array.add(randint(0, 255))
    return list(array)


def reverse_right_part_array(array):
    start = len(array) // 2
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


def sort_array(array):
    array.sort()
    reverse_right_part_array(array)


def converter_array_to_start_impulse(array):
    if length_is_odd(len(array)):
        sort_array(array)
        return array
    else:
        return None

# def converter_array_to_start_impulse(array):
#     if length_is_odd(len(array)):
#         array.sort()
#         right_part_array = array[len(array) // 2:]
#         array[len(array) // 2:] = right_part_array[::-1]
#         return array
#     else:
#         return None
