import numpy as np


class BoardUtility:

    @staticmethod
    def has_player_won(game_board, player_piece):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        # checking horizontally
        for r in range(3):
            if game_board[r][0] == player_piece and game_board[r][1] == player_piece and game_board[r][
                2] == player_piece:
                return True

        # checking vertically
        for c in range(3):
            if game_board[0][c] == player_piece and game_board[1][c] == player_piece and game_board[2][
                c] == player_piece:
                return True

        # checking diagonally
        if game_board[0][0] == player_piece and game_board[1][1] == player_piece and game_board[2][
            2] == player_piece:
            return True

        if game_board[0][2] == player_piece and game_board[1][1] == player_piece and game_board[2][
            0] == player_piece:
            return True

        return False

    @staticmethod
    def is_draw(game_board):
        return not np.any(game_board == 0)

    @staticmethod
    def score_position(game_board, piece):
        """
        compute the game board score for a given piece.
        you can change this function to use a better heuristic for improvement.
        """
        piece = 1
        opponent = 2
        if BoardUtility.is_draw(game_board):
            return 0
        if BoardUtility.has_player_won(game_board, piece):
            return 100_000_000_000  # player has won the game give very large score
        if BoardUtility.has_player_won(game_board, opponent):
            return -100_000_000_000  # player has lost the game give very large negative score
        # todo score the game board based on a heuristic.
        else:

            finalList = []
            for i in range(3):
                lineList = []
                for j in range(3):
                    lineList.append(game_board[i][j])
                finalList.append(lineList)
            for i in range(3):
                lineList = []
                lineList.append(game_board[0][i])
                lineList.append(game_board[1][i])
                lineList.append(game_board[2][i])
                finalList.append(lineList)
            lineList = []
            for i in range(3):
                lineList.append(game_board[i][i])
            finalList.append(lineList)
            lineList = []
            lineList.append(game_board[0][2])
            lineList.append(game_board[2][0])
            lineList.append(game_board[1][1])
            finalList.append(lineList)
            score = BoardUtility.evaluation(finalList, piece, opponent)

        return score

    @staticmethod
    # took from https://www3.ntu.edu.sg/home/ehchua/programming/java/javagame_tictactoe_ai.html
    def evaluation(lineList, me, opponent):
        score = 0
        for i in range(len(lineList)):
            if lineList[i].count(me) == 1 and lineList[i].count(opponent) == 1:
                continue
            if lineList[i].count(me) == 2 and lineList[i].count(opponent) == 0:
                score += 100
                continue
            if lineList[i].count(opponent) == 2 and lineList[i].count(me) == 0:
                score -= 100
                continue
            if lineList[i].count(opponent) == 1 and lineList[i].count(me) == 0:
                score -= 10
                continue
            if lineList[i].count(me) == 1 and lineList[i].count(opponent) == 0:
                score += 10
                continue
        return score

    @staticmethod
    def get_valid_locations(game_board):
        """
        returns all the valid locations to make a move.
        """
        valid_locations = []

        for i in range(3):
            for j in range(3):
                if game_board[i, j] == 0:
                    valid_locations.append((i, j))
        return valid_locations

    @staticmethod
    def is_terminal_state(game_board):
        """
        return True if either of the player have won the game or we have a draw.
        """
        return BoardUtility.has_player_won(game_board, 1) or BoardUtility.has_player_won(game_board,
                                                                                         2) or BoardUtility.is_draw(
            game_board)

    @staticmethod
    def make_move(game_board, row, col, player):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """
        assert game_board[row][col] == 0
        game_board[row][col] = player
