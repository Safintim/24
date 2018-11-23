from random import choice


def pprint(matrix):
    for row in matrix:
        print(''.join(str(i) for i in row), sep='\n')
    print()


def convert_text_image_to_array(text_image):
    return [symbol if symbol == '.' else 1
            for symbol in text_image
            if symbol not in [' ', '\n']]


def create_start_matrix(rows, columns, text_image):
    array_symbols = convert_text_image_to_array(text_image)
    start = 0
    matrix = []
    for i in range(rows):
        matrix.append(array_symbols[start:start+columns])
        start += columns

    return matrix


def generate_random_text_image(row, column):
    dot_or_plus = ['.', '+']
    return ''.join([choice(dot_or_plus) for _ in range(row * column)])


def increase_age_by_one_year(matrix):
    branches_older_than_or_equal_three = []
    for row, row_value in enumerate(matrix):
        for column, value in enumerate(row_value):

            if value == '.':
                row_value[column] = 1
            else:
                row_value[column] += 1

            if row_value[column] >= 3:
                branches_older_than_or_equal_three.append((row, column))

    return branches_older_than_or_equal_three


def death_branch():
    return '.'


def is_left(column):
    if column >= 0:
        return True


def is_right(column, len_row):
    if column < len_row:
        return True


def is_up(row):
    if row >= 0:
        return True


def is_down(row, count_row):
    if row < count_row:
        return True


def death_branches(matrix, branches):
    if not branches:
        return False
    for (row, column) in branches:

        matrix[row][column] = death_branch()

        if is_left(column - 1):
            matrix[row][column-1] = death_branch()
        if is_right(column + 1, len(matrix[row])):
            matrix[row][column + 1] = death_branch()
        if is_up(row - 1):
            matrix[row - 1][column] = death_branch()
        if is_down(row + 1, len(matrix)):
            matrix[row + 1][column] = death_branch()


def simulate_life_tree(matrix, age):
    pprint(matrix)
    for year in range(age+1):
        if year <= 1:
            continue

        branches_older_than_or_equal_three = increase_age_by_one_year(matrix)
        if year % 2 == 1:
            death_branches(matrix, branches_older_than_or_equal_three)
        pprint(matrix)


def tree_of_life_andrassyl(rows, columns, age, text_image=None):
    if not text_image:
        text_image = generate_random_text_image(rows, columns)

    matrix = create_start_matrix(rows, columns, text_image)
    simulate_life_tree(matrix, age)
