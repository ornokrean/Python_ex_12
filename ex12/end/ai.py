#############################################################################
# FILE : ai.py
# WRITER : or nokrean , ornokrean , 206223166
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: exercise for building ai that plays alone at the four in a row
#               game,  this file is the AI class that finds a legal move and
#               plays it in given game
#############################################################################
from random import shuffle


class AI:
    """
    this class is the ai for the four in a row game, deciding randomly in
    which not full column to place a new disc of the ai player at his turn
    """
    __NO_MOVES_ERROR = "No possible AI moves."

    def find_legal_move(self, game, func, timeout=None):
        """
        this function finds a legal move - a random column to add a disc to,
        and runs the given func with th column. if the function doesn't
        find a column, it throws an exception of NO_MOVES_ERROR.
        :param game: the game that is played
        :param func: the func to run with the column found
        :param timeout: the max time the function needs to run
        """
        columns = [i for i in range(game.COLUMNS) if
                   game.get_column_length(i) < game.ROWS]
        if columns:
            shuffle(columns)
            func(columns[0])
        else:
            raise Exception(self.__NO_MOVES_ERROR)
