# -*- coding: utf-8 -*-
__author__ = 'krudenko@ucsd.edu, kdduong@ucsd.edu, a9dang@ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
	
	def max_turn(self, state, alpha, beta):
		if(state.is_terminal()):
			return state.utility(self)

		# Grabs possible actions
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Lowest possible utility first	
		best_utility = -2

		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.min_turn(new_state, alpha, beta)

			if(current_utility > best_utility):
				best_utility = current_utility
				best_action = action
			if best_utility >= beta:
				return best_utility
			if alpha < best_utility:
				alpha = best_utility

		return best_utility


	def min_turn(self, state, alpha, beta):
		if(state.is_terminal()):
			return state.utility(self)
		# Grabs possible actions
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Highest possible utility first	
		best_utility = 2

		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.max_turn(new_state, alpha, beta)
			if(current_utility < best_utility):
				best_utility = current_utility
				best_action = action
			if best_utility <= alpha:
				return best_utility
			if beta > best_utility:
				beta = best_utility

		return best_utility

	def move(self, state):
		"""Calculates the best move from the given board using the minimax algorithm.

		Args:
			state (State): The current state of the board.

		Returns:
			the next move (Action)
		"""

		# TODO implement this
		# depth is used to distinguish between really good moves and just good moves

		# We start with calculating min because we are in perspective of max
		# Grabs possible actions
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Lowest possible utility first	
		best_utility = -2
		alpha = -100
		beta = 100

		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.min_turn(new_state, alpha, beta)

			if(current_utility > best_utility):
				best_utility = current_utility
				best_action = action

		return best_action