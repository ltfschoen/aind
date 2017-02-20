import sys; assert sys.version_info >= (3,6,0)
from utils import display, boxes

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

def get_peers_for_box(box, boxes):
    """
    Input: Box i.e. B3
    Output: Array of peer boxes associated with given box, including those in its same unit/square, and same row and column,
    but not including the box being processed itself (as we do not want to eliminate from its value from itself)
    """

    # ROW - get boxes from array whose property string starts with same letter
    boxes_with_same_row = list(filter(lambda x : x[0] == box[0], boxes))
    boxes_with_same_row.remove(box) # remove current box from result as we do not want to eliminate it

    # COL - get boxes from array whose property number is same number
    boxes_with_same_col = list(filter(lambda x : x[1] == box[1], boxes))
    boxes_with_same_col.remove(box) # remove current box from result as we do not want to eliminate it

    # SQUARE BOXES - get all boxes that are within the same unit/square as the given box so we can eliminate them
    boxes_with_same_square = get_boxes_in_unit(box, boxes)
    boxes_with_same_square.remove(box) # remove current box from result as we do not want to eliminate it

    # COMBINE - combine all the peers for elimination
    combined = []
    combined = boxes_with_same_row + boxes_with_same_col + boxes_with_same_square

    # REMOVE DUPLICATES - remove any duplicates added to the combined list (not really necessary though)
    combined_unique = list(set(combined))

    return combined_unique

def eliminate(values):
    """
    Input: Puzzle in dictionary form.
    Output: Iterate over all boxes in puzzle that only have one value assigned to them,
    remove this value from every one of its peers, and return puzzle in dictionary form
    """

    # find all boxes with only 1 value
    solved_values = [box for box in values.keys() if len(values[box]) == 1]

    # iterate through each box that only has 1 value
    for box in solved_values:
        digit = values[box]
        peers = get_peers_for_box(box, boxes)
        # iterate through each peer associated with the box with only 1 value and eliminate the value from each
        for peer in peers:
            values[peer] = values[peer].replace(digit,'')
    return values

# Visualisation of Sudoku puzzle generated in dictionary form
result = grid_values(unsolved_puzzle)
vis = display(result)
output = eliminate(result)
print(output)
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