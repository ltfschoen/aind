import sys; assert sys.version_info >= (3,6,0)
from utils import display, boxes

# Board - concatenation of reading digits left to right in rows from top to bottom using . as empty box placeholder
unsolved_puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
solved_puzzle = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'

def grid_values(grid):
    """ Convert string representation of a Sudoku puzzle into a {<box>: <value>}
    dictionary representation with '.' value for empty values

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
        - i.e.
            {
              'A1': '.'
              'A2': '.',
              'A3': '3',
              'A4': '.',
              'A5': '2',
              ...
              'I9': '.'
            }
    """
    #    # Course Solution:
    #    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    #    return dict(zip(boxes, grid))

    # My Solution
    return dict(map(lambda x: x, zip(boxes, grid)))

# Visualisation of Sudoku puzzle generated in dictionary form
""" Outputs:
  . . 3 |. 2 . |6 . .
  9 . . |3 . 5 |. . 1
  . . 1 |8 . 6 |4 . .
  ------+------+------
  . . 8 |1 . 2 |9 . .
  7 . . |. . . |. . 8
  . . 6 |7 . 8 |2 . .
  ------+------+------
  . . 2 |6 . 9 |5 . .
  8 . . |2 . 3 |. . 9
  . . 5 |. 1 . |3 . .
"""

display(grid_values(unsolved_puzzle))