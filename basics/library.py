def hamming_for_strings(current_status, goal_state):
    distance = 0
    i = 0
    for letter in current_status:
        if letter != goal_state[i]:
            distance += 1
        i += 1
    return distance


def list_to_string(list_to_convert):
    return '\n'.join(['-'.join(row) for row in list_to_convert])


def string_to_list(string_to_convert):
    return [row.split('-') for row in string_to_convert.split('\n')]


def find_location(matrix, element_to_find):
    for array_position, array in enumerate(matrix):
        for array_element, element in enumerate(array):
            if element == element_to_find:
                return array_position, array_element
