from abc import ABC

from simpleai import search
from basics import library as lib
from basics import constants as cts

goal_positions = {}
rows_goal = lib.string_to_list(cts.eight_eight_puzzle_goal)
for number in '12345678e':
    goal_positions[number] = lib.find_location(rows_goal, number)


class EightPuzzleProblem(search.SearchProblem, ABC):
    def actions(self, current_state):
        rows = lib.string_to_list(current_state)
        row_e, col_e = lib.find_location(rows, 'e')

        actions = []
        if row_e > 0:
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, current_state, next_action):
        rows = lib.string_to_list(current_state)
        row_e, col_e = lib.find_location(rows, 'e')
        row_n, col_n = lib.find_location(rows, next_action)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return lib.list_to_string(rows)

    def is_goal(self, current_state):
        return current_state == cts.eight_eight_puzzle_goal

    def cost(self, next_action, state_1, state_2):
        return 1

    def heuristic(self, current_state):
        distance = lib.hamming_for_strings(current_state, cts.eight_eight_puzzle_goal)
        return distance


result = search.astar(EightPuzzleProblem(cts.eight_eight_puzzle_initial_1))

for action, state in result.path():
    print('Move number', action)
    print(state)
