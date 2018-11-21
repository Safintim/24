from itertools import permutations


def get_all_permutations_string(string):
    all_permutations = []
    for p in permutations(string):
        all_permutations.append(''.join(p))

    return all_permutations


def is_possible(string):
    if reversed(string) == string or string.count(string[0]) == len(string):
        return False
    return True


def get_magic_word_from_string(string):
    if is_possible(string):

        all_permutations = get_all_permutations_string(string)
        all_permutations.sort()
        index_string = all_permutations.index(string)
        return all_permutations[index_string + 1]
    else:
        return None


"""второй способ"""


def swap_first_with_large(symbols):
    max_symbol = max(symbols)
    for index, symbol in enumerate(symbols):
        if symbols[0] < symbol <= max_symbol:
            max_symbol = symbol
            index_need_symbol = index
    symbols[index_need_symbol], symbols[0] = symbols[0], max_symbol
    return symbols


def make_line_min(symbols, start=0):
    right_part_symbols = symbols[start + 1:]
    right_part_symbols.sort()
    symbols[start + 1:] = right_part_symbols
    return symbols


def make_line_more(symbols):
    start = len(symbols)-1
    is_swap = False
    while start and not is_swap:
        for i in range(start, 1, -1):
            next_symbol = i-1
            if symbols[start] > symbols[next_symbol]:
                symbols[start], symbols[next_symbol] = (symbols[next_symbol],
                                                        symbols[start])
                # is_swap = True
                make_line_min(symbols, next_symbol)
                return symbols
        start -= 1
    return None


def get_magic_word_from_string(string):
    if not is_possible(string):
        return False

    symbols = list(string)
    is_magic_word = make_line_more(symbols)
    if not is_magic_word:
        swap_first_with_large(symbols)
        make_line_min(symbols)
    return ''.join(symbols)
