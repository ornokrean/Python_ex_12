#############################################################################
# FILE : game.py
# WRITER : or nokrean , ornokrean , 206223166
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: exercise for building game logic that runs the four in a row
#                game,  this file is the Game class that handles all the logic
#                   of the game
#############################################################################


class Game:
    """
    this class is responsible on the logic side of the four in a row game,
    handling all situations in the game
    """
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2
    TURN = "turn"
    WIN = "win"
    ILLEGAL_MOVE_EXCEPTION = "Illegal move."
    __DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]
    __WIN_AMOUNT = 4
    COLUMNS = 7
    ROWS = 6
    HUMAN = "human"
    AI = "ai"
    ROW_FORMAT_FACTOR = 1
    START_OF_LST = 0
    SEARCH_RANGE = (-3, 1)

    def __init__(self):
        """
        this function initializes the game and its attributes
        """
        self.__board_content = {i: list() for i in range(self.COLUMNS)}
        self.__player = str(Game.PLAYER_ONE)
        self.__last_disc_placed = None
        self.__game_winner = False
        self.__player_type = self.HUMAN
        self.__ai = None

    def make_move(self, column):
        """
        this function makes a move in the game if the given column is valid
        and have space for another disc, and if the game is not won yet.
        if all is good, it places a disc and changes the player turn
        :param column: the column to add disc to
        :return: status, move_player, winning_places when:
                status: the game status - win, draw or regular turn
                move_player: the player who made the move
                winning_places: none if no win yet, a list of coordinates
                                if the game was won
        """

        # check for column validity
        if column is None or (column < self.START_OF_LST or column >=
                              self.COLUMNS):
            raise Exception(self.ILLEGAL_MOVE_EXCEPTION)

        # get the amount of discs in given column
        col_items = len(self.__board_content[column])

        # check for col_items validity or if game won
        if col_items >= self.ROWS or self.__game_winner:
            raise Exception(self.ILLEGAL_MOVE_EXCEPTION)

        # add the disc to column if all is good
        self.__board_content[column].append(self.get_current_player())
        self.__last_disc_placed = (col_items, column)

        # check game status, and get the playing player and winning places
        # (if needed)
        status, move_player, winning_places = self.__game_handler()

        # move on to next player
        self.__change_player()

        return status, move_player, winning_places

    def get_winner(self):
        """
        this function returns the "status" of the game:
         - player code if the game is won
         - Game.DRAW if draw is made
         - none otherwise - regular turn or during the game
        :return: as described above
        """
        if self.__game_winner:
            # do not check again if we already have a winner
            return int(self.__game_winner)
        winner = self.__find_winner()
        if winner:
            # return the player who won
            return int(self.__game_winner)
        draw = self.__check_for_draw()
        if draw:
            return self.DRAW

    def get_player_at(self, row, col):
        """
        this function finds the player at given coordinates
        :param row: the row of the place wanted
        :param col: the column of the place wanted
        :return: the player code if there is a player there, none otherwise
        """
        row = self.__format_row_to_board(row)
        if row < self.ROWS and col < self.COLUMNS and row < len(
                self.__board_content[col]):
            return self.__board_content[col][row]
        return

    def __format_row_to_board(self, row):
        """
        this function reverse the row - column for the way board_content is
        built
        :param row: the row to format
        :return: the new formatted row
        """
        return self.ROWS - row - self.ROW_FORMAT_FACTOR

    def get_current_player(self):
        """
        this function returns the current player in the game
        :return: the current player code in the game
        """
        return self.__player

    def __game_handler(self):
        """
        this function handles the game routine, checks for winner, otherwise
        for draw and if not returns regular turn
        :return: tuple of:
                    the game status: win / draw / turn
                    the current player: player code
                    winning places: if there is a win, the winning places
                                    are the places found to make the win,
                                    returns as a list, none otherwise
        """
        winner_places = self.__find_winner()

        if winner_places:
            # win
            return str(Game.WIN), self.__game_winner, winner_places

        draw = self.__check_for_draw()
        if draw:
            # draw
            return str(Game.DRAW), self.get_current_player(), None

        # regular turn
        return str(Game.TURN), self.get_current_player(), None

    def __change_player(self):
        """
        this function switches between the players
        """
        self.__player = str(Game.PLAYER_TWO) if self.__player == str(
            Game.PLAYER_ONE) else str(Game.PLAYER_ONE)

    def __check_for_draw(self):
        """
        this function checks for draw in the game, if all column are full
        its a draw (we will call it if we don't have a winner)
        :return: true if there is a draw, false otherwise
        """
        draw = True
        for index in self.__board_content:
            if len(self.__board_content[index]) != self.ROWS:
                draw = False
        return draw

    def __find_winner(self):
        """
        this function finds a winner, by checking the last played disc
        surrounding for all directions and possibles matches for win,
        and return list containing all winning places if there is, or empty
        list otherwise
        :return: list containing all winning places if there is, or empty
                    list otherwise
        """
        if self.__last_disc_placed:
            row, column = self.__last_disc_placed
            places = list()
            for direction in self.__DIRECTIONS:

                for i in range(self.SEARCH_RANGE[0], self.SEARCH_RANGE[1]):
                    start = self.__new_location((row, column), direction, i)
                    cur_places = list()
                    for j in range(self.__WIN_AMOUNT):
                        step = self.__new_location(start, direction, j)
                        if self.__check_valid_location(step) and \
                                self.__board_content[column][row] == \
                                self.__board_content[step[1]][step[0]]:
                            step = (
                                self.__format_row_to_board(step[0]), step[1])
                            cur_places.append(step)
                    if len(cur_places) == self.__WIN_AMOUNT:
                        places.append(cur_places)
            if places:
                self.__game_winner = self.__board_content[column][row]
            return places

    def __new_location(self, start, step, multiplier):
        """
        this function finds the new location by the step and multiplier given,
        used for __find_winner function
        :param start: tuple, the place to start from
        :param step: tuple, the step we need to make
        :param multiplier: int, the number to multiply the step by
        :return: new tuple of coordinates, x,y
        """
        x = start[0] + step[0] * multiplier
        y = start[1] + step[1] * multiplier
        return x, y

    def __check_valid_location(self, location):
        """
        this function checks if the given location is a valid location on
        the board, and if the column given of the location is not full
        :param location: the location to check
        :return: true if the location is valid as described above,
                    false otherwise
        """
        return self.START_OF_LST <= location[
            0] < self.ROWS and self.START_OF_LST <= location[
                   1] < self.COLUMNS and location[0] < len(
            self.__board_content[location[1]])

    def set_player_type(self, type):
        """
        this function sets the player type if the type is valid
        :param type: the type to change to
        """
        if type == self.HUMAN or type == self.AI:
            self.__player_type = type

    def get_player_type(self):
        """
        this function returns the game player type
        :return: the game player type
        """
        return self.__player_type

    def set_ai(self, ai):
        """
        this function sets the ai
        :param ai: the ai to set
        """
        self.__ai = ai

    def get_column_length(self, column):
        """
        this function returns the length of given column in board_content
        :param column: the column that we want to return its length
        :return: int, the length of given column in board_content
        """
        return len(self.__board_content[column])

    def ai_move(self, func):
        """
        this function makes the ai move when the player type is ai
        :param func: the function for find_legal_move to make after a move
                        was found
        """
        try:
            self.__ai.find_legal_move(self, func)
        except:
            return
