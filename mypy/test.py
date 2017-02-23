import logging
import typing; from typing import *

# MyPy Lint should be run with `mypy test.py`
# def get_list_for_str(word: str) -> None:
def get_list_for_str(word: str) -> typing.List[str]:
    return word.split(',')

my_str = "1,2,3"
my_list = get_list_for_str(my_str)

def run():

    try:
        my_str = "1,2,3"
        my_list = get_list_for_str(my_str)
        assert type(my_list) is list, "my_list is a List: %r" % my_list
        logging.debug("Trying app")

    except:
        logging.exception('Exception occurred.')

if __name__ == '__main__':
    run()