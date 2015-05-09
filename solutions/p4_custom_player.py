# -*- coding: utf-8 -*-
__author__ = 'krudenko@ucsd.edu, kdduong@ucsd.edu, a9dang@ucsd.edu'

from assignment2 import Player, State, Action


class YourCustomPlayer(Player):
    @property
    def name(self):
        """Returns the name of this agent. Try to make it unique!"""
        return 'HAL9000'

    def move(self, state):
        """Calculates the absolute best move from the given board position using magic.
        
        Args:
            state (State): The current state of the board.

        Returns:
            your next Action instance
        """
        visited = {}
        actions = []
        depth_limit = 6

        for d in range(1, depth_limit):
            possible_actions = state.actions()
            best_move = state.actions()[0]
            best_value = -1.0
            alpha = -100
            beta = 100
            depth = 0
            for action in possible_actions:
                new_state = state.result(action)
                actions.insert(0, (action, self.min_value(new_state, alpha, beta, visited, depth+1, d)))
        actions.sort(key = lambda a: a[1])
        best_move = actions[len(actions)-1]
        return best_move[0]

    def max_value(self, state, alpha, beta, transposition_table, depth, depth_limit):
        # If time is up or we reached the depth limit, evaluate and return!
        if self.is_time_up() or depth == depth_limit:
            return self.evaluate(state, self.color)

        if state.is_terminal():
            transposition_table[state] = state.utility(self)
            return state.utility(self)
        # Grabs possible actions
        possible_actions = state.actions()
        best_action = possible_actions[0]
        # Lowest possible utility first 
        best_utility = -2

        for action in possible_actions:
            if transposition_table.get(state.result(action)) is None:
                new_state = state.result(action)
                current_utility = self.min_value(new_state, alpha, beta, transposition_table, depth+1, depth_limit)
            else:
                current_utility = transposition_table[state.result(action)]
            if(current_utility > best_utility):
                best_utility = current_utility
                best_action = action
            if best_utility >= beta:
                return best_utility
            if alpha < best_utility:
                alpha = best_utility
        return best_utility

    def min_value(self, state, alpha, beta, transposition_table, depth, depth_limit):
        # If time is up or we reached the depth limit, evaluate and return!
        if self.is_time_up() or depth == depth_limit:
            return -self.evaluate(state, self.color)

        if state.is_terminal():
            transposition_table[state] = state.utility(self)
            return state.utility(self)

        # TODO something here
        possible_actions = state.actions()
        best_action = possible_actions[0]
        # Highest possible utility first    
        best_utility = 2

        for action in possible_actions:
            if transposition_table.get(state.result(action)) is None:
                new_state = state.result(action)
                current_utility = self.max_value(new_state, alpha, beta, transposition_table, depth+1, depth_limit)
            else:
                current_utility = transposition_table[state.result(action)]
            if(current_utility < best_utility):
                best_utility = current_utility
                best_action = action
            if best_utility <= alpha:
                return best_utility
            if beta > best_utility:
                beta = best_utility
        return best_utility

    def evaluate(self, state, color):
        """Evaluates the state for the player with the given stone color.
        1.0 is a definite win, -1.0 is a definite loss (same scale as the utility)."""
        streak = []
        #iterate through the board:
        for i in range(0, state.M):
            for j in range(0, state.N):
                if (state.board[i][j] == color):
                    streak.insert(0, self.streak(state.board, i, j))
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
