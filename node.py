import numpy as np


class Node:
    
    def __init__(self, board=None, parent=None, action=None, move_cost=0, path_cost=0, depth=0, h1=0, h2=0, h3=0):
        self.board = board
        self.parent = parent
        self.action = action
        self.move_cost = move_cost # g(n)
        self.path_cost = path_cost
        self.depth = depth
        self.blank_index = self.board.index(0)
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.goal = (1,2,3,8,0,4,7,6,5)
        
    # Override for node board comparison in queues and stacks for repeate state checking
    def __eq__(self, other):
        return self.board == other.board

    
    # Override for use with __eq__
    def __hash__(self):
        return hash(self.board)
    
    # Get num of misplaced tiles
    def get_h1(self):
        for i in range(len(self.board)):            
            if self.board[i] != self.goal[i]:
                self.h1 += 1
                    
    # Get manhattan distance of each tile
    def get_h2(self):        
        h2 = 0 
        for i in range(len(self.board)):
            x = abs((self.board.index(i)//3) - self.goal.index(i)//3)
            y = abs((self.board.index(i)%3) - self.goal.index(i)%3)
            h2 = x + y
        self.h2 = h2
        
    # Get manhattan * tile value of each tile
    def get_h3(self):
        h3 = 0
        for i in range(len(self.board)):
            x = abs((self.board.index(i)//3) - self.goal.index(i)//3)
            y = abs((self.board.index(i)%3) - self.goal.index(i)%3)
            h3 = (x + y) * self.board[i]
        self.h3 = h3
        
    # Check if goal state
    def isGoal(self):
        return self.board == self.goal 
               
    # Swap two tiles. 
    # Converts board tuple to array, makes swap, then returns new tuple
    def swap(self, i, j):
        new_board_array = list(self.board)
        new_board_array[i], new_board_array[j] = new_board_array[j], new_board_array[i]
        return tuple(new_board_array)
        
    # Successor function. Get children of this node
    def get_children(self):
        row = np.floor(self.blank_index / 3)
        col = self.blank_index % 3
        children = []   
        
        # Move down
        if row == 0 or row == 1: 
            new_board = self.swap(self.blank_index, self.blank_index + 3)
            move_cost = self.board[self.blank_index + 3]
            path_cost = self.path_cost + move_cost
            depth = self.depth + 1
            children.append(Node(new_board, self, 'down', move_cost, path_cost, depth))
        # Move up
        if row == 1 or row == 2: 
            new_board = self.swap(self.blank_index, self.blank_index - 3)
            move_cost = self.board[self.blank_index - 3]
            path_cost = self.path_cost + move_cost
            depth = self.depth + 1
            children.append(Node(new_board, self, 'up', move_cost, path_cost, depth))
        # Move right
        if col == 0 or col == 1: 
            new_board = self.swap(self.blank_index, self.blank_index + 1)
            move_cost = self.board[self.blank_index + 1]
            path_cost = self.path_cost + move_cost
            depth = self.depth + 1
            children.append(Node(new_board, self, 'right', move_cost, path_cost, depth))
        # Move left
        if col == 1 or col == 2: 
            new_board = self.swap(self.blank_index, self.blank_index - 1)
            move_cost = self.board[self.blank_index - 1]
            path_cost = self.path_cost + move_cost
            depth = self.depth + 1
            children.append(Node(new_board, self, 'left', move_cost, path_cost, depth))
        return children