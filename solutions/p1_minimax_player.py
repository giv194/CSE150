# -*- coding: utf-8 -*-
__author__ = 'krudenko@ucsd.edu, kdduong@ucsd.edu, a9dang@ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
	
	# This is a recursive helper method for move() to determine the utility for the node in pov of max
	def max_turn(self, state):

		# Base case: Did we reach an end state?
		if(state.is_terminal()):
			# Determines and returns utility of that node
			return state.utility(self)

		# Grabs possible actions to perform on this state
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Lowest possible utility first	
		best_utility = -2

		# Loop through each action, determine resulting state, determine utility,
		# is it the best utility in pov of max?
		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.min_turn(new_state)

			if(current_utility > best_utility):
				best_utility = current_utility
				best_action = action

		return best_utility

	# This is a recursive helper method for move() to determine the utility for the node in pov of min
	def min_turn(self, state):
		# Base case: Did we reach an end state?
		if(state.is_terminal()):
			# Determines and returns utility of that node
			return state.utility(self)
			
		# Grabs possible actions to perform on this state	
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Highest possible utility first	
		best_utility = 2

		# Loop through each action, determine resulting state, determine utility,
		# is it the best utility in pov of min?
		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.max_turn(new_state)

			if(current_utility < best_utility):
				best_utility = current_utility
				best_action = action

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
		# Grabs possible actions to perform on this state
		possible_actions = state.actions()
		best_action = possible_actions[0]
		# Lowest possible utility first	
		best_utility = -2

		# Loop through each action, determine resulting state, determine utility,
		# is it the best utility in pov of max?
		for action in possible_actions:
			new_state = state.result(action)
			current_utility = self.min_turn(new_state)

			# We are using best utility to determine the best action.
			if(current_utility > best_utility):
				best_utility = current_utility
				best_action = action

		return best_action

