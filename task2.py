def remove_duplicates_in_array(array):
    unique_elem = set()
    for elem in array:
        if elem not in unique_elem:
            yield elem
            unique_elem.add(elem)


def select_place_from_top_list(top_list, prize):
    for index, elem in enumerate(top_list, 1):
        if prize >= elem:
            return index
        elif index == len(top_list):
            return index + 1


def get_history_successes(top_list, successes_data_team):
    history_successes = []
    sum_prev_results = 0
    top_list = list(remove_duplicates_in_array(top_list))
    for prize in successes_data_team:
        sum_prev_results += prize
        place = select_place_from_top_list(top_list, sum_prev_results)
        history_successes.append(place)

    return history_successes
