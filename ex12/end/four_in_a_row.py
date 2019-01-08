#############################################################################
# FILE : four_in_a_row.py
# WRITER : or nokrean , ornokrean , 206223166
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: exercise for building gui that runs the four in a row game,
#               this file is the GUI class and the main of the game
#############################################################################
import socket
from tkinter import *
from communicator import Communicator
from game import *
import random
import sys
import ai

# Legal run variables:
MIN_PORT = 0
MAX_PORT = 65535
CLIENT_ARGS_LENGTH = 4
SERVER_ARGS_LENGTH = 3
ARGS_ERROR = "Illegal program arguments."
EMPTY_STRING = ""

# Game variables:
MSG_PLAYER_POS = 1
MSG_COL_POS = -2
MSG_START = "<"
MSG_END = ">"
EXIT_GAME_MSG_BODY = "exit_game"
EXIT_GAME_MSG = MSG_START + EXIT_GAME_MSG_BODY + MSG_END
MSG_BODY = " place at column "
MIN_COUNT_FOR_MSG_END = 1
VALID_MSG_POS = -2

# Files:
ONE_BALL_IMG = "blue.png"
TWO_BALL_IMG = "red.png"
EMPTY_CELL = "empty.png"
EXIT_BTN = "exit.png"
EXIT_BTN_HOVER = "exit_hover.png"
ONE_WIN_IMG = "blue_win.png"
TWO_WIN_IMG = "red_win.png"
BOARD_BG = "board.gif"

# Titles:
ONE_TITLE = "Player One - Blue"
TWO_TITLE = "Player Two - Red"

# Colors and design:
PLAYER_ONE_COLOR = "#006eda"
PLAYER_TWO_COLOR = "#a30606"
DRAW_COLOR = "#952ba8"
BACKGROUND = "#42210b"
HOVER_COLOR = "#b79e58"
LOCK_COLOR = "#934722"
HEADER_COLOR = "#E9C86E"
WIN_COLOR = "#FFD700"
HEADER_FONT = "Tolkien"
HEADER_PAD_Y = 15
HEADER_FONT_SIZE = 20
LABEL_PAD_Y = 3
LABEL_PAD_X = 4
BOARD_PADDING = 13
COLOR_CODE = '#%02X%02X%02X'
COLORS = (0, 255)
TEXT_DECORATION = "bold"

# Header label text:
YOUR_TURN_LABEL = "Your Turn"
YOU_WON_LABEL = "You Won!"
YOU_LOST_LABEL = " You Lost :("
PLAYER_ONE_LABEL = "Player 1's Turn"
PLAYER_ONE_WIN = "Player 1 Won!"
PLAYER_TWO_LABEL = "Player 2's Turn"
PLAYER_TWO_WIN = "Player 2 Won!"
DRAW_LABEL = "It's a DRAW!"


class GUI:
    """
    this class is responsible on the gui and handling the game changes,
    connecting to the other player and sending and receiving messages trough
    the communicator, and showing the game
    """

    def __init__(self, parent, human, port, ip=None):
        """
        this function is used to initialize the gui element
        :param parent: the root of the gui
        :param human: the type of player
        :param port: port to connect to
        :param ip: ip to connect to
        """
        self.__root = parent

        # set player code
        if ip:
            self.__player = str(Game.PLAYER_TWO)
        else:
            self.__player = str(Game.PLAYER_ONE)

        # create game elements
        self.__get_game_elements()
        self.__create_board_header()
        self.__game = Game()

        # set player type in game
        self.__game.set_player_type(human)
        if self.__player_is_ai():
            ai_for_game = ai.AI()
            self.__game.set_ai(ai_for_game)

        # create board elements
        self.__board_cells = dict()
        self.__create_board_elements()

        # connent to communicator
        self.__communicator_init(port, ip)

        # make the first move if player one and ai
        if self.__player == str(Game.PLAYER_ONE) and \
                self.__player_is_ai():
            self.__ai_move()

    def __create_board_elements(self):
        """
        this function creates the board element on the screen
        """
        self.__board_container = Label(self.__root, image=self.__board_bg,
                                       bg=PLAYER_ONE_COLOR)
        self.__board_container.pack()
        self.__board = Frame(self.__board_container)
        self.__board.place(x=BOARD_PADDING, y=BOARD_PADDING)
        self.__create_game_board()

    def __communicator_init(self, port, ip):
        """
        this function connects to the communicator
        :param port: port to connect to
        :param ip: ip to connect to
        """
        self.__communicator = Communicator(self.__root, port, ip)
        self.__communicator.connect()
        self.__communicator.bind_action_to_message(self.__handle_message)

    def __ai_move(self):
        """
        this function makes the ai move when the player type is ai
        """
        self.__game.ai_move(self.__column_clicked)

    def __handle_message(self, text=None):
        """
        this function handles the message receive during the game
        :param text: the message that was sent
        """
        if text:
            text = self.__fix_message(text)
            if EXIT_GAME_MSG in text or not self.__communicator.is_connected():
                self.__end_game()
            else:
                column = int(text[MSG_COL_POS])
                player = text[MSG_PLAYER_POS]
                if player != self.__game.get_current_player():
                    self.__column_clicked(column, True)

    def __send_message(self, text):
        """
        this function send a message using the communicator
        :param text: the message to br sent
        """
        if text == EXIT_GAME_MSG:
            message = text
        else:
            message = MSG_START + str(self.__game.get_current_player()) + \
                      MSG_BODY + str(text) + MSG_END
        self.__communicator.send_message(message)

    def __fix_message(self, message):
        """
        this function fixes the message given if we got two messages together
        :param message: the message to be fix
        :return: the fixed message if needed, otherwise the original message
        """
        if message.count(MSG_END) > MIN_COUNT_FOR_MSG_END:
            message = message.split(MSG_END)[VALID_MSG_POS] + MSG_END
        return message

    def __create_game_board(self):
        """
        this function creates the game board using create_cell function
        """
        for row in range(Game.ROWS):
            for column in range(Game.COLUMNS):
                self.__create_cell(row, column, self.__empty_cell)

    def __create_cell(self, row, column, image, color=BACKGROUND):
        """
        this function creates a new cell in the board in given location
        :param row: row location of cell
        :param column: column location of cell
        :param image: the image for the cell to present
        :param color: the background color of the cell
        """
        if (row, column) in self.__board_cells:
            color = self.__board_cells[(row, column)].cget("bg")
        new_label = Label(self.__board, image=image, padx=LABEL_PAD_X,
                          pady=LABEL_PAD_Y, bg=color)
        if not self.__player_is_ai():
            new_label.bind("<Button-1>",
                           lambda event: self.__column_clicked(column))
        enter = self.__create_column_hover(column, HOVER_COLOR)
        new_label.bind("<Enter>", enter)
        leave = self.__create_column_hover(column, BACKGROUND)
        new_label.bind("<Leave>", leave)
        new_label.grid(row=row, column=column)
        self.__board_cells.update({(row, column): new_label})

    def __create_board_header(self):
        """
        this function creates the game board header, with status label and
        exit button
        """
        self.__root.config(bg=PLAYER_ONE_COLOR)
        # create header label
        text = PLAYER_ONE_LABEL
        if self.__player == str(Game.PLAYER_ONE):
            text = YOUR_TURN_LABEL
        self.__status_label = Label(self.__root, text=text,
                                    fg=HEADER_COLOR, bg=PLAYER_ONE_COLOR,
                                    font=(
                                        HEADER_FONT, HEADER_FONT_SIZE,
                                        TEXT_DECORATION),
                                    pady=HEADER_PAD_Y)
        self.__status_label.pack(side=TOP)

        # create exit button
        self.__exit_game = Label(self.__root, image=self.__exit_btn,
                                 bg=PLAYER_ONE_COLOR)
        self.__exit_game.pack(side=TOP)
        self.__exit_game.bind("<Enter>", lambda event: self.__exit_game.config(
            image=self.__exit_btn_hover))
        self.__exit_game.bind("<Leave>", lambda event: self.__exit_game.config(
            image=self.__exit_btn))
        self.__exit_game.bind("<Button-1>", self.__end_game)

    def __change_status(self, status, player):
        """
        this function changes the status label of the game
        :param status: the new status code
        :param player: the player to change the board to - this player turn
        """
        text = EMPTY_STRING
        color = PLAYER_ONE_COLOR
        if player == str(Game.PLAYER_ONE):
            color = PLAYER_TWO_COLOR
        if status == str(Game.TURN):
            if player == str(Game.PLAYER_TWO):
                text = PLAYER_ONE_LABEL
            elif player == str(Game.PLAYER_ONE):
                text = PLAYER_TWO_LABEL
            if player != self.__player:
                text = YOUR_TURN_LABEL
        elif status == str(Game.WIN):
            if player == str(Game.PLAYER_ONE):
                text = PLAYER_ONE_WIN
            elif player == str(Game.PLAYER_TWO):
                text = PLAYER_TWO_WIN
            if player != self.__player:
                text += YOU_LOST_LABEL
            else:
                text = YOU_WON_LABEL
        elif status == str(Game.DRAW):
            text = DRAW_LABEL
            color = DRAW_COLOR
        self.__change_board_elements(color, text)

    def __change_board_elements(self, color, text=EMPTY_STRING):
        """
        this function changes all relevant elements on board to given color
        and text
        :param color: the color to change to
        :param text: the text to change to
        """
        if text:
            self.__status_label.config(text=text, bg=color)
            self.__root.config(bg=color)
            self.__exit_game.config(bg=color)
            self.__board_container.config(bg=color)

    def __column_clicked(self, column, msg=False):
        """
        this function decides what to do when a column was clicked
        :param column: the column where the click was made
        :param msg: bool, whether we got the click trough a message or not
        """
        if self.__not_current_player() and not msg:
            return
        try:
            status = self.__game.make_move(column)
        except:
            return
        if status:
            status, player, winning_places = status
            self.__add_ball(column, player)
            self.__change_status(status, player)
            if status == str(Game.WIN):
                self.__game_won(player, winning_places)
            if self.__not_current_player():
                self.__send_message(column)
            elif self.__player_is_ai():
                self.__ai_move()

    def __game_won(self, winner, winning_places):
        """
        this function is called when the game is won, ang it changes all the
        needed changes for the winning status, and shows the winning places
        on the board
        :param winner: str, the winner  of the game - the player code
        :param winning_places: the places who won the game
        """
        win_img = self.__one_winner
        if winner == str(Game.PLAYER_TWO):
            win_img = self.__two_winner

        for column in range(Game.COLUMNS):
            self.__lock_column(column, True)
        for x, y in winning_places[0]:
            self.__board_cells[(x, y)].config(image=win_img, bg=WIN_COLOR)

    def __create_column_hover(self, column, color):
        """
        this function creates the column hover function individually,
        for the user to easily see and play
        :param column: the column to create hover to
        :param color: the color od the hover
        :return: the function __column_hover
        """

        def __column_hover(event=None):
            """
            this function creates column hover, for every cell in the column
            :param event: the event triggered the hover
            """
            for row in range(Game.ROWS):
                self.__board_cells[(row, column)].config(bg=color)

        return __column_hover

    def __end_game(self, event=None):
        """
        this function ends the game, send a message to the other gui and exits
        :param event: the event of clicking the element in order to end the
        game
        """
        self.__send_message(EXIT_GAME_MSG)
        self.__root.quit()

    def __get_game_elements(self):
        """
        this function loads all the relevant images for the game board
        """
        self.__one_ball = PhotoImage(file=ONE_BALL_IMG)
        self.__two_ball = PhotoImage(file=TWO_BALL_IMG)
        self.__empty_cell = PhotoImage(file=EMPTY_CELL)
        self.__exit_btn = PhotoImage(file=EXIT_BTN)
        self.__exit_btn_hover = PhotoImage(file=EXIT_BTN_HOVER)
        self.__one_winner = PhotoImage(file=ONE_WIN_IMG)
        self.__two_winner = PhotoImage(file=TWO_WIN_IMG)
        self.__board_bg = PhotoImage(file=BOARD_BG)

    def __add_ball(self, column, player):
        """
        this function adds the given ball to the board in the given column
        :param column: the column that was picked by the player
        :param player: the player who played
        """
        if player == str(Game.PLAYER_ONE):
            ball = self.__one_ball
        elif player == str(Game.PLAYER_TWO):
            ball = self.__two_ball
        else:
            return
        row = Game.ROWS - self.__game.get_column_length(column)
        color = BACKGROUND
        if self.__not_current_player() and \
                not self.__player_is_ai():
            color = HOVER_COLOR

        self.__create_cell(row, column, ball, color)
        if not row:
            self.__lock_column(column)

    def __lock_column(self, column, end_game=False):
        """
        this function "locks" the given column only visually for the user
        to see that the column cant be picked
        :param column: the column to lock
        """

        color = LOCK_COLOR
        for row in range(Game.ROWS):
            if end_game:
                color = self.__random_color()
            enter = self.__create_column_hover(column, color)

            if self.__not_current_player() or (color != LOCK_COLOR and
                    not end_game and self.__player_is_ai()):
                self.__board_cells[(row, column)].config(bg=color)
                self.__board_cells[(row, column)].bind("<Enter>", enter)
                if end_game:
                    self.__board_cells[(row, column)].bind("<Leave>", enter)
            if not end_game:
                self.__board_cells[(row, column)].bind("<Enter>", enter)

    def __random_color(self):
        """
        this function randoms a color for the winner board to celebrate his win
        :return: the color that was randomized
        """

        def r():
            """
            this function returns a random number between 0 and 255
            :return:  a random number between 0 and 255
            """
            return random.randint(COLORS[0], COLORS[1])

        return COLOR_CODE % (r(), r(), r())

    def __player_is_ai(self):
        """
        this function checks and returns if the player of this gui is ai or not
        :return: True if the player type is ai, False otherwise
        """
        return self.__game.get_player_type() == Game.AI

    def __not_current_player(self):
        """
        this function checks and returns if the player of this gui is the
        current player in the game or not
        :return: True if the player is not the current player, False if he
                    is the current player
        """
        return self.__player != self.__game.get_current_player()


def main():
    """
    main of the program, checks for args validity and runs the game if args
    are valid
    """
    root = Tk()
    args_length = len(sys.argv)

    # first we check for all the given args validity:
    # human (argv[1]) is "human" or "ai"
    # port (argv[2]) is between 0 to 65535
    # args length is 3 or 4
    if SERVER_ARGS_LENGTH <= args_length <= CLIENT_ARGS_LENGTH and \
            MIN_PORT <= int(sys.argv[2]) <= MAX_PORT and \
            (sys.argv[1] == Game.HUMAN or sys.argv[1] == Game.AI):
        if args_length == CLIENT_ARGS_LENGTH:
            # client gui
            print (socket.gethostbyname(socket.gethostname()))
            GUI(root, sys.argv[1], int(sys.argv[2]), sys.argv[3])
            # GUI(root, sys.argv[1], int(sys.argv[2]), socket.gethostbyname(
            #     socket.gethostname()))
            # GUI(root, sys.argv[1], int(sys.argv[2]), "0.0.0.0")

            # set the title
            root.title(TWO_TITLE)

        elif args_length == SERVER_ARGS_LENGTH:
            # server gui
            GUI(root, sys.argv[1], int(sys.argv[2]))
            # set the title
            root.title(ONE_TITLE)

        # run the gui
        root.mainloop()
    else:
        # print error message if args are invalid
        print(ARGS_ERROR)


if __name__ == '__main__':
    main()
