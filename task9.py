def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1


def find_all_indexes_substring(a_str, arr):
    substring_indexes = []
    for elem in arr:
        current_indexes_substring = list(find_all(a_str, elem))
        if current_indexes_substring:
            substring_indexes.append(current_indexes_substring)
    return substring_indexes


def is_second_in_first(delimiter, substring_indexes):
    for row in range(len(substring_indexes)):
        s = {i+int(delimiter) for i in substring_indexes[row]}
        if row < len(substring_indexes)-1:
            if not s.intersection(substring_indexes[row+1]):
                return False
    return True


def is_second_arr_in_first_arr(first_arr, second_arr):
    rows1, columns1, *first_arr = first_arr.split()
    rows2, columns2, *second_arr = second_arr.split()

    first_arr = ''.join(first_arr)
    substring_indexes = find_all_indexes_substring(first_arr, second_arr)

    if not (len(substring_indexes) == int(rows2) and
            is_second_in_first(columns1, substring_indexes)):
        return False

    return True


'''input:
first_arr = 4 6 029402 560202 029694 780288
second_arr = 2 2 02 94

output:
True/False
'''
