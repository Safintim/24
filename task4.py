from itertools import permutations


def get_all_permutations_string(string):
    all_permutations = []
    for p in permutations(string):
        all_permutations.append(''.join(p))

    return all_permutations


def is_possible(string):
    if string.count(string[0]) != len(string):
        return True
    else:
        return False


def get_magic_word_from_string(string):
    if is_possible(string):

        all_permutations = get_all_permutations_string(string)
        all_permutations.sort()
        index_string = all_permutations.index(string)
        return all_permutations[index_string + 1]
    else:
        return None


