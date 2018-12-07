def get_repeating_element(seq):
    values_seq = {}
    for i in seq:
        if i in values_seq:
            values_seq[i] += 1
        else:
            values_seq[i] = 1
    return values_seq


def is_valid(string):
    count_reps_symbols = get_repeating_element(string)
    count_all_repetitions = get_repeating_element(count_reps_symbols.values())
    _, max_count_reps = max(zip(count_all_repetitions.values(), count_all_repetitions.keys()))

    if len(count_all_repetitions) == 1:
        return True
    elif len(count_all_repetitions) > 2:
        return False
    else:

        for key, value in list(count_reps_symbols.items()):
            if max_count_reps == value:
                count_reps_symbols.pop(key)

        if len(count_reps_symbols) == 2:
            return False
        else:
            _, last_value = count_reps_symbols.popitem()
            if last_value - 1 == 0 or last_value - 1 == max_count_reps:
                return True
            else:
                return False
