import copy
class Winner:
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2
    TURN = "turn"
    WIN = "win"
    UPWARDS = 'u'
    LINEAR_RIGHT = 'r'
    DOWN_AND_RIGHT = 'y'
    UP_AND_RIGHT = 'w'
    DIRECTIONS = UPWARDS + LINEAR_RIGHT + DOWN_AND_RIGHT + UP_AND_RIGHT
    WIN_AMOUNT = 4
    ONE_WIN = str(PLAYER_ONE)*WIN_AMOUNT
    TWO_WIN = str(PLAYER_TWO)*WIN_AMOUNT
    ONE_WIN_VAL = str(PLAYER_ONE)
    TWO_WIN_VAL = str(PLAYER_TWO)
    EMPTY_SLOT = "X"
    COLUMNS =7


    def format_matrix(self,columns_content):
        output = list()
        col = copy.deepcopy(columns_content)
        for i in sorted(col):
            lst_len = len(col[i])
            if lst_len < self.COLUMNS:
                for j in range(self.COLUMNS - lst_len):
                    col[i].append(self.EMPTY_SLOT)
            output.append(col[i])
        return output


    def get_loop_params(self,matrix, direction):
        """
        this function gets params of matrix and direction and returns the
        appropriate lat_length and loops range for the matrix_search function
        :param matrix: a matrix
        :param direction: one of ALLOWED_DIRECTIONS
        :return: lst_length - int, length of the new list to be created
                 first_loop_range - int, range for the first loop
                 second_loop_range - int, range for the second loop
        """
        lst_length = 0
        first_loop_range = range(0)
        second_loop_range = range(0)
        matrix_len = len(matrix)

        if matrix_len == 0:
            # matrix is empty, return default values
            return lst_length, first_loop_range, second_loop_range

        inside_matrix_len = 7

        if inside_matrix_len == 0:
            # inner matrix is empty, return default values
            return lst_length, first_loop_range, second_loop_range

        if direction == self.LINEAR_RIGHT:
            lst_length = inside_matrix_len
            first_loop_range = range(inside_matrix_len)
            second_loop_range = range(matrix_len)

        elif direction == self.UPWARDS:
            lst_length = len(matrix)
            first_loop_range = range(matrix_len)
            second_loop_range = range(inside_matrix_len)

        elif direction == self.DOWN_AND_RIGHT:
            lst_length = (len(matrix) + inside_matrix_len - 1)
            first_loop_range = range(matrix_len)
            second_loop_range = range(inside_matrix_len - 1, -1, -1)

        elif direction == self.UP_AND_RIGHT:
            lst_length = (matrix_len + inside_matrix_len - 1)
            first_loop_range = range(matrix_len)
            second_loop_range = range(inside_matrix_len)

        return lst_length, first_loop_range, second_loop_range


    def matrix_search(self,matrix, direction):
        """
        this function searches in the given matrix by the given direction(s)
        :param matrix: a matrix of letters
        :param direction: directions given by the user
        :return: a list containing all strings found in given direction(s)
        """
        # first, get loop params from get_loop_params function
        lst_length, first_loop_range, second_loop_range = self.get_loop_params(
            matrix, direction)
        search_result = [""] * lst_length
        for i in first_loop_range:
            for j in second_loop_range:
                if direction == self.LINEAR_RIGHT:

                    search_result[i] += matrix[j][i]

                elif direction == self.DOWN_AND_RIGHT:
                    # x, y
                    search_result[i - j] += matrix[i][j]
                elif direction == self.UP_AND_RIGHT:
                    # z,w
                    search_result[i + j] += matrix[i][j]
                elif direction == self.UPWARDS:
                    search_result[i] += matrix[i][j]

        return search_result


    def find_in_matrix(self,matrix, directions):
        """
        this function returns all the strings from given matrix according to the
        directions given, using a loop to go over each direction separately.
        :param matrix: a matrix of letters (list of words)
        :param directions: a string containing the directions for the matrix search
        :return: list containing all the strings from given matrix according to
        the directions given
        """
        matrix_results = []
        for direction in directions:
            result = self.matrix_search(matrix, direction)
            if result is not []:
                matrix_results += [element.lower() for element in result]
        return matrix_results


    def sort_results(self,results):
        """
        this function gets a dictionary with the search results in matrix,
        and creates an alphabetically sorted list of the keys with values bigger
        then DEFAULT_DICTIONARY_VALUE, in format of "key,val" in each list place
        :param results: the dictionary containing the search results in matrix
        :return: a list in format of "key,val" in each list place, val being
        bigger then DEFAULT_DICTIONARY_VALUE
        """
        for result in results:
            if len(result) > 3:
                if self.ONE_WIN in result:
                    return str(self.PLAYER_ONE)
                elif self.TWO_WIN in result:
                    return str(self.PLAYER_TWO)
        return None

    def check_for_win(self,columns_content):
        matrix = self.format_matrix(columns_content)
        results = self.find_in_matrix(matrix, self.DIRECTIONS)
        return self.sort_results(results)

