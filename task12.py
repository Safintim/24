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
        n = 0
        for key, value in list(count_reps_symbols.items()):
            if max_count_reps != value:
                n += 1
                if value - 1 != 0 and value - 1 != max_count_reps:
                    flag = True
                else:
                    flag = False

        else:
            if n == 2 or flag:
                return False

    return True

