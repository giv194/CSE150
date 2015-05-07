# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

import heapq

from assignment2 import Player


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-ply look-ahead with a simple evaluation function.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """

        # *You do not need to modify this method.*
        best_move = None
        max_value = -1.0
        my_color = state.to_play.color

        for action in state.actions():
            if self.is_time_up():
                break

            result_state = state.result(action)
            value = self.evaluate(result_state, my_color)
            if value > max_value:
                max_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, color):
        """Evaluates the state for the player with the given stone color.

        This function calculates the length of the longest ``streak'' on the board
        (of the given stone color) divided by K.  Since the longest streak you can
        achieve is K, the value returned will be in range [1 / state.K, 1.0].

        Args:
            state (State): The state instance for the current board.
            color (int): The color of the stone for which to calculate the streaks.

        Returns:
            the evaluation value (float), from 1.0 / state.K (worst) to 1.0 (win).
        """
        streak = []
        #iterate through the board:
        for i in range(0, state.M):
            for j in range(0, state.N):
                if (state.board[i][j] == color):
                    streak.insert(0, self.streak(state.board, i, j))
        # TODO implement this
        streak.sort();
        return float(streak[len(streak)-1])/state.K

    def streak(self, board, i, j):
        toreturn = 1
        longest = 1
        x = i
        y = j
        #in line
        for y in range(j+1, len(board[0]) - 1):
            if board[x][y] == board[i][j]:
                longest = longest + 1
            else:   
                break
        toreturn = longest
        #in column
        longest = 1
        y = j
        for x in range(i+1, len(board) - 1):
            if board[x][y] == board[i][j]:
                longest = longest + 1
            else:
                break
        if (longest > toreturn):
            toreturn = longest
        longest = 1
        x = i+1
        y = j+1

        while (x < len(board)) and (y < len(board[0])):
            if board[x][y] == board[i][j]:
                longest = longest + 1
                x = x + 1
                y = y + 1
            else:
                break
        if (longest > toreturn):
            toreturn = longest

        longest = 1
        x = i+1
        y = j-1
        while (x < len(board)) and (y >= 0):
            if board[x][y] == board[i][j]:
                longest = longest + 1
                x = x + 1
                y = y - 1
            else:
                break
        if (longest > toreturn):
            toreturn = longest
        return toreturn





