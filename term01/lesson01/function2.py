import sys; assert sys.version_info >= (3,6,0)
from utils import display, boxes, unitlist
from utils import peers
import functools
import copy

# Board
unsolved_puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """ Convert grid string of a Sudoku puzzle into a {<box>: <value>}
    dictionary representation with '123456789' value for empty values

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
        - i.e.
            {
              'A1': '123456789'
              'A2': '123456789',
              'A3': '3',
              'A4': '123456789',
              'A5': '2',
              ...
              'I9': '123456789'
            }
    """
    #    # Course Solution:
    #    values = []
    #        all_digits = '123456789'
    #        for c in grid:
    #            if c == '.':
    #                values.append(all_digits)
    #            elif c in all_digits:
    #                values.append(c)
    #        assert len(values) == 81
    #        return dict(zip(boxes, values))

    # My Solution
    result = dict(map(lambda x: x, zip(boxes, grid)))
    for k, v in result.items():
        if v == '.':
            result[k] = '123456789'
    return result

def get_boxes_in_unit(box, boxes):
    """
    Input: Box i.e. B3
    Output: Array of all the boxes in the same unit/square as the given box (including the box itself)
    """
    unit1 = boxes[0:3] + boxes[9:12] + boxes[18:21]
    unit2 = boxes[3:6] + boxes[12:15] + boxes[21:24]
    unit3 = boxes[6:9] + boxes[15:18] + boxes[24:27]
    unit4 = boxes[27:30] + boxes[36:39] + boxes[45:48]
    unit5 = boxes[30:33] + boxes[39:42] + boxes[48:51]
    unit6 = boxes[33:36] + boxes[42:45] + boxes[51:54]
    unit7 = boxes[54:57] + boxes[63:66] + boxes[72:75]
    unit8 = boxes[57:60] + boxes[66:69] + boxes[75:78]
    unit9 = boxes[60:63] + boxes[69:72] + boxes[78:81]

    if box in unit1:
        return unit1
    if box in unit2:
        return unit2
    if box in unit3:
        return unit3
    if box in unit4:
        return unit4
    if box in unit5:
        return unit5
    if box in unit6:
        return unit6
    if box in unit7:
        return unit7
    if box in unit8:
        return unit8
    if box in unit9:
        return unit9

# def get_peers_for_box(box, boxes):
#     """
#     Input: Box i.e. B3
#     Output: Array of peer boxes associated with given box, including those in its same unit/square, and same row and column,
#     but not including the box being processed itself (as we do not want to eliminate from its value from itself)
#     """
#
#     # ROW - get boxes from array whose property string starts with same letter
#     boxes_with_same_row = list(filter(lambda x : x[0] == box[0], boxes))
#     boxes_with_same_row.remove(box) # remove current box from result as we do not want to eliminate it
#
#     # COL - get boxes from array whose property number is same number
#     boxes_with_same_col = list(filter(lambda x : x[1] == box[1], boxes))
#     boxes_with_same_col.remove(box) # remove current box from result as we do not want to eliminate it
#
#     # SQUARE BOXES - get all boxes that are within the same unit/square as the given box so we can eliminate them
#     boxes_with_same_square = get_boxes_in_unit(box, boxes)
#     boxes_with_same_square.remove(box) # remove current box from result as we do not want to eliminate it
#
#     # COMBINE - combine all the peers for elimination
#     combined = []
#     combined = boxes_with_same_row + boxes_with_same_col + boxes_with_same_square
#
#     # REMOVE DUPLICATES - remove any duplicates added to the combined list (not really necessary though)
#     combined_unique = list(set(combined))
#
#     return combined_unique

def eliminate(values):
    # """
    # Input: Puzzle in dictionary form.
    # Output: Iterate over all boxes in puzzle that only have one value assigned to them,
    # remove this value from every one of its peers, and return puzzle in dictionary form
    # """
    #
    # # find all boxes with only 1 value
    # solved_values = [box for box in values.keys() if len(values[box]) == 1]
    #
    # # iterate through each box that only has 1 value
    # for box in solved_values:
    #     digit = values[box]
    #     peers = get_peers_for_box(box, boxes)
    #     # iterate through each peer associated with the box with only 1 value and eliminate the value from each
    #     for peer in peers:
    #         values[peer] = values[peer].replace(digit,'')
    # return values
    #
    # update_dict = values
    # for i in update_dict:
    #     if len(update_dict[i]) == 1:
    #         peer_values = peers[i]
    # digit = update_dict[i]
    # for v in peer_values:
    #     update_dict[v] = update_dict[v].replace(digit,'')
    # return (update_dict)

    update_dict = values
    for k, v in update_dict.items():
        if len(update_dict[k]) == 1:
            peer_keys = peers[k]
            digit = update_dict[k]
            for pk in peer_keys:
                update_dict[pk] = update_dict[pk].replace(digit,'')
    return update_dict

def only_choice(values):
    """
    Finalize all values that are the only choice for a unit.

    Go through all the units/squares, and whenever there is a unit with
    a box that contains an unsolved value that only fits in that one box,
    assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in Only Choices.
    """

    # Course Solution:
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

    # # My Solution (Marked Incorrect):
    #
    # # print("values: ", values)
    #
    # latest_dict = copy.deepcopy(values)
    # temp_dict = copy.deepcopy(values)
    # update_dict = values
    # for box, val in update_dict.items():
    #     # SQUARE BOX - get all boxes that are within the same unit/square as the given box
    #     # print("box: ", box)
    #     boxes_in_same_square_as_box = get_boxes_in_unit(box, boxes)
    #     # print("boxes in same square: ", boxes_in_same_square_as_box)
    #
    #     # create deep copy of original dict and remove any boxes that are not in square of current box
    #     copy_update_dict = copy.deepcopy(update_dict)
    #     for k in update_dict:
    #         if not k in boxes_in_same_square_as_box:
    #             del copy_update_dict[k]
    #     # print(copy_update_dict)
    #
    #     # create deep copy of dict containing all boxes in square and remove any boxes with only 1 value
    #     square_dict = copy.deepcopy(copy_update_dict)
    #     for k in copy_update_dict:
    #         if len(copy_update_dict[k]) == 1:
    #             del square_dict[k]
    #     # print("square_dict with unsolved boxes: ", square_dict)
    #
    #     if len(square_dict) != 0:
    #         # create list of all the values (including duplicates) from unsolved boxes in current square
    #         unsolved_boxes_keys = []
    #         unsolved_boxes_values = []
    #         for k, v in square_dict.items():
    #             unsolved_boxes_keys.append(k)
    #             unsolved_boxes_values.append(v)
    #         # print(unsolved_boxes_keys)
    #         # print(unsolved_boxes_values)
    #         all_unsolved_boxes_values = functools.reduce(lambda x,y: x+y, unsolved_boxes_values)
    #         # print("all_unsolved_boxes_values: ", all_unsolved_boxes_values)
    #
    #         list_unresolved = list(all_unsolved_boxes_values)
    #         uniq = set(list_unresolved)
    #         # print("uniq: ", uniq)
    #         only_ones = [] # there may be more than one box in a square having a value that only occurs
    #         # once in unsolved boxes of that square
    #         for u in uniq:
    #             if all_unsolved_boxes_values.count(u) == 1:
    #                 only_ones.append(u)
    #         # print("only ones: ", only_ones)
    #
    #         # update relevant boxes in temp_dict to be returned (overwrite the remaining possibilities with
    #         # the only one for that box
    #         temp_dict = latest_dict
    #         for k, v in latest_dict.items():
    #             if k in unsolved_boxes_keys:
    #                 for o in only_ones:
    #                     if o in v:
    #                         # print("only one: ", o)
    #                         # print("v is: ", v)
    #                         index_of_only_one = only_ones.index(o)
    #                         # print("index of only one: ", index_of_only_one)
    #                         temp_dict[k] = only_ones[index_of_only_one]
    #         latest_dict = temp_dict
    #         # print("updated latest_dict: ", latest_dict)
    #
    # print(latest_dict)
    # return latest_dict

def reduce_puzzle(values):
    """
    Constraint Propagation Technique applied.
    Input: Unsolved Sudoku puzzle as dict
    Process: Apply repeatedly the eliminate() and only_choice() functions
    as constraints. Stop and return puzzle when solved. Exit loop by returning
    False when stuck at box with no available values. If Sudoku puzzle unchanged
    after iterating both eliminate() and only_choice() functions then return the Sudoku
    Output: Solution to Sudoku puzzle as dict
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

# Visualisation of Sudoku puzzle generated in dictionary form
result = grid_values(unsolved_puzzle)
vis = display(result)
output = eliminate(result)
print(output)
# output2 = only_choice(output)
output2 = reduce_puzzle(output)
print(output2)

""" Sample Output:
  45   4578   3   |  9     2     17  |  6    5789   57
  9   24678   47  |  3     47    5   |  78   278    1
  25   257    1   |  8     79    6   |  4   23579  2357
------------------+------------------+------------------
 345   345    8   |  1    356    2   |  9   34567 34567
  7    2359   9   |  59   3569   4   |  1    356    8
 1345 13459   6   |  7    359    8   |  2    345   345
------------------+------------------+------------------
 134   1347   2   |  6     78    9   |  5    1478   47
  8    1467   47  |  2     57    3   |  7    1467   9
  6    679    5   |  4     1     7   |  3    2678  267
"""