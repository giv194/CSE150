# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'
 
from assignment2 import Player, State, Action
from operator import itemgetter

class MinimaxPlayer(Player):
	def minimax_helper(self, state):
		#gets legal moves
 		moves = state.actions()

		solutions = []
		visited = {}
		for x in moves:
			solutions.insert(0, (x, self.min_turn(state.result(x), visited)))
		
		#sort by utility attribute, the second item in the tuple
		solutions.sort(key = lambda a: a[1])
		
		
		Res = solutions[len(solutions)-1]
		return Res[0]

	def move(self, state):
		return self.minimax_helper(state)


 	
	def max_turn(self, state, visited):
		if state.is_terminal():
			visited[state] = state.utility(self)
			return state.utility(self)
		moves = state.actions()
        
        
		solutions = []
		
		for x in moves:
			if visited.get(state.result(x)) is not None:
				solutions.insert(0, (x, visited[state.result(x)]))
			else:
				solutions.insert(0, (x, self.min_turn(state.result(x), visited)))
        	
        #sort by utility attribute, the second item in the tuple
		solutions.sort(key=lambda a: a[1])
        
		Res = solutions[len(solutions)-1]
		
		return Res[1]
 		
 
	def min_turn(self, state, visited):
		if state.is_terminal():
			visited[state] = state.utility(self)
			return state.utility(self)
		moves = state.actions()
        
        
		solutions = []
		
		for x in moves:
			if visited.get(state.result(x)) is not None:
				solutions.insert(0, (x, visited[state.result(x)]))
			else:
				solutions.insert(0, (x, self.max_turn(state.result(x), visited)))
        	
        #sort by utility attribute, the second item in the tuple
		solutions.sort(key=lambda a: a[1])
        
		Res = solutions[0]
		return Res[1]
		