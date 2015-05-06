# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def move(self, state):
        """Calculates the best move from the given board using the minimax algorithm.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """
        moves = state.actions()
        best_move = state.actions()[0]
        best_util = -2
        for move in moves:
        	next_state = state.result(move)
        	current_util = min_turn(self, next_state)
        	if current_util > best_util:
        		best_move = move
        		best_util = current_util
        return best_move

    def max_turn(self, state):
    	if state.is_terminal():
    		return state.utility()
    	moves = state.actions()
    	best_util = -2
    	for move in moves:
        	next_state = state.result(move)
        	current_util = min_turn(self, next_state)
        	if current_util > best_util:
        		best_move = move
        		best_util = current_util
        return best_util


    def min_turn(self, state):
    	if state.is_terminal():
    		return state.utility()
    	moves = state.actions()
    	best_util = 2
    	for move in moves:
        	next_state = state.result(move)
        	current_util = max_turn(next_state)
        	if current_util < best_util:
        		best_move = move
        		best_util = current_util
        return best_util





