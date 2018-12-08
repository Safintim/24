from random import shuffle


def try_ascending_sort(array):
    array_sort = sorted(array)
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            elem_out_of_place = array[i]
            index_elem_out_of_place = i

            for j in range(index_elem_out_of_place + 1, len(array)):

                if elem_out_of_place > array[j]:

                    swap_two_elements_in_array(array, j, index_elem_out_of_place)
                    if is_sort(array, array_sort):
                        return True
                    swap_two_elements_in_array(array, index_elem_out_of_place, j)

                    reverse_part_in_array(array, index_elem_out_of_place, j)
                    if is_sort(array, array_sort):
                        return True
                    reverse_part_in_array(array, index_elem_out_of_place, j)
            break
    return False


def swap_two_elements_in_array(array, i, j):
    array[i], array[j] = array[j], array[i]


def reverse_part_in_array(array, start, end):
    array[start:end + 1] = array[start:end + 1][::-1]


def is_sort(array, array_sort):
    return array == array_sort
