import math


def remove_all_space_in_string(string):
    return string.replace(' ', '')


def calculate_size_matrix(length):
    sqrt_length = math.sqrt(length)
    row = math.floor(sqrt_length)
    column = math.ceil(sqrt_length)

    if row * column < length:
        row += 1

    return int(row), int(column)


def string_without_space_to_array(string):
    return [symbol for symbol in string]


def create_matrix(row, column):
    return [[None] * column for _ in range(row)]


def add_string_to_matrix(string, matrix):
    column = len(matrix[0])
    start = 0
    for row, value in enumerate(matrix):
        matrix[row] = string_without_space_to_array(
            string[start:column + start])
        start += column

    return matrix


def add_encrypted_string_to_matrix(string, matrix):

    for column in range(len(matrix[0])):
        start = 0
        for row, value in enumerate(matrix):
            if len(string[column]) > row:
                matrix[row][column] = string[column][start]
                start += 1


def return_encrypted_string(matrix):
    cipher = ''
    for column in range(len(matrix[0])):
        for row in matrix:
            if len(row) > column:
                cipher += row[column]
        cipher += ' '
    return cipher.strip()


def return_decrypted_string(matrix):
    source_code = ''
    for row in matrix:
        source_code += ''.join(symbol if symbol is not None else '' for symbol in row)
    return source_code


def encrypted_string(string):
    string_without_space = remove_all_space_in_string(string)
    row, column = calculate_size_matrix(len(string_without_space))
    matrix = create_matrix(row, column)
    add_string_to_matrix(string_without_space, matrix)
    return return_encrypted_string(matrix)


def decrypted_string(string):
    string_without_space = remove_all_space_in_string(string)
    row, column = calculate_size_matrix(len(string_without_space))
    matrix = create_matrix(row, column)
    add_encrypted_string_to_matrix(string.split(), matrix)
    return return_decrypted_string(matrix)


print('отдай мою кроличью лапку - test1')
enc_str = encrypted_string('отдай мою кроличью лапку')
print(enc_str)
decr_str = decrypted_string(enc_str)
print(decr_str)
print()

print('Бобер нас раскрыли - test2')
enc_str = encrypted_string('Бобер нас раскрыли')
print(enc_str)
decr_str = decrypted_string(enc_str)
print(decr_str)
print()

print('Орел вылетел - test3')
enc_str = encrypted_string('Орел вылетел')
print(enc_str)
decr_str = decrypted_string(enc_str)
print(decr_str)