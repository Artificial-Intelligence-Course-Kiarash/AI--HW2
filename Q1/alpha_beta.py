import copy
import math
import random

import Board


def minimax(board, player_piece, depth, max_depth, is_maximizing_player, alpha, beta):
    """
    This function run alpha beta puring algorithm and return best next move
    :param board: game board
    :param player_piece: number of player. 1 or 2
    :param depth: depth of tree
    :param is_maximizing_player: True if you are in a max node otherwise False
    :param alpha: value of alpha
    :param beta: value of beta
    :return best_value, best_move: You have to return best next move and its value
    """
    if Board.BoardUtility.has_player_won(board, 1):
        return 100_000_000_000, (0, 0)
    elif Board.BoardUtility.has_player_won(board, 2):
        return -100_000_000_000, (0, 0)
    elif Board.BoardUtility.is_draw(board):
        return 0, (0, 0)

    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                list.append((i, j))
    if depth == max_depth:
        score = Board.BoardUtility.score_position(board, player_piece)
        return score, (0, 0)

    if is_maximizing_player:
        score = -1 * math.inf
    else:
        score = math.inf
    best_move = None
    for i in list:
        newBoard = copy.deepcopy(board)
        newBoard[i[0]][i[1]] = player_piece

        if player_piece == 1:
            res = minimax(newBoard, 2, depth + 1, max_depth, False, 0, 0)
        else:
            res = minimax(newBoard, 1, depth + 1, max_depth, True, 0, 0)
        if is_maximizing_player:
            if res[0] > score:
                score = res[0]
                alpha = max(alpha, score)
                best_move = i
                if beta <= alpha:
                    break
        else:
            if res[0] < score:
                score = res[0]
                beta = min(beta, score)
                best_move = i
                if beta <= alpha:
                    break
    return score, best_move

    # TODO : fill me
    pass


def minimax_prob(board, player_piece, depth, max_depth, is_maximizing_player, alpha, beta, prob):
    """
    This function run alpha beta puring algorithm and return best next move
    :param board: game board
    :param player_piece: number of player. 1 or 2
    :param depth: depth of tree
    :param is_maximizing_player: True if you are in a max node otherwise False
    :param alpha: value of alpha
    :param beta: value of beta
    :param prob: probability of choosing a random action in each max node
    :return best_value, best_move: You have to return best next move and its value
    """
    if Board.BoardUtility.has_player_won(board, 1):
        return 100_000_000_000, (0, 0)
    elif Board.BoardUtility.has_player_won(board, 2):
        return -100_000_000_000, (0, 0)
    elif Board.BoardUtility.is_draw(board):
        return 0, (0, 0)

    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                list.append((i, j))
    if depth == max_depth:
        score = Board.BoardUtility.score_position(board, player_piece)
        return score, (0, 0)

    if is_maximizing_player:
        score = -1 * math.inf
    else:
        score = math.inf
    best_move = None
    my_possible_moves = []
    for i in list:
        newBoard = copy.deepcopy(board)
        newBoard[i[0]][i[1]] = player_piece

        if player_piece == 1:
            res = minimax(newBoard, 2, depth + 1, max_depth, False, 0, 0)
        else:
            res = minimax(newBoard, 1, depth + 1, max_depth, True, 0, 0)
        if is_maximizing_player:
            if res[0] > score:
                my_possible_moves.append((res[0], i))
                alpha = max(alpha, res[0])
                if beta <= alpha:
                    break
        else:
            if res[0] < score:
                score = res[0]
                best_move = i
                beta = min(beta, res[0])
                if beta <= alpha:
                    break
    if is_maximizing_player:
        random_number = random.random()
        if random_number < prob or len(my_possible_moves) == 1:
            return my_possible_moves[-1][0], my_possible_moves[-1][1]
        else:
            my_possible_moves.pop()
            random_move = random.choice(my_possible_moves)
            return random_move[0], random_move[1]
    else:
        return score, best_move
    # TODO fill me
    pass
