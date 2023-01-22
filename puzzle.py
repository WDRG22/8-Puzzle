import numpy as np
from copy import deepcopy
from collections import deque

    
class Node:
    board = None
    depth = 0
    action = None
    parent = None
    children = []
    move_cost = 0
    path_cost = 0
    expanded = False
    
    def __init__(self, board, parent=None, children=[], depth=0, path_cost=0, move_cost=0, action=None, expanded=False):
        self.board = board
        self.depth = depth
        self.parent = parent
        self.action = action
        self.children = children
        self.move_cost = move_cost
        self.path_cost = path_cost
        self.expanded = expanded
        self.blank_index = self.board.index(0)
        
    def isGoal(self):
        return self.board == (1,2,3,8,0,4,7,6,5)
        
    def print_board(self):
        print(self.board)

    # Print all fields of this node
    def print_node(self):
        print(
            f'\nBoard: {self.board}\n'
            f'Depth: {self.depth}\n'
            f'Action: {self.action}\n'
            f'Parent: {self.parent}\n'
            f'Children: {self.children}\n'
            f'Path Cost: {self.path_cost}\n'
            f'Expanded: {self.expanded}\n'
            )
             
    def print_children(self):
        for child in self.children:
            child.print_board()
                
    def get_blank_index(self):
        return self.board.index(0)
     
    # Checks is given move is valid based on index of blank tile
    def get_possible_moves(self):    
        index = self.get_blank_index()
        row = np.floor(index / 3)
        col = index % 3    
        
        if row == 0:
            if col == 0:
                possible_moves = ["right", "down"]
            elif col == 1:                
                possible_moves = ["right", "left", "down"]
            else:
                possible_moves = ["left", "down"]                
        elif row == 1:
            if col == 0:
                possible_moves = ["up", "right", "down"]
            elif col == 1:
                possible_moves = ["up", "right", "left", "down"]
            else:
                possible_moves = ["up", "left", "down"]
        else:
            if col == 0:
                possible_moves = ["up", "right"]
            elif col == 1:
                possible_moves = ["up", "right", "left"]
            else:
                possible_moves = ["up", "left"]        
        return possible_moves     
     
    # Make move on this node's board if valid
    def move(self, move):
        possible_moves = self.get_possible_moves()
        if move in possible_moves:
            self.board = self.makeMove(move)
        else:
            print('"{move}" is not a valid move')
     
    # Moves blank tile. Returns tuple containing new board and value of tile swapped 
    # with blank tile. Move validation should occur outside method call
    def make_move(self, move):                        
        if move == 'up':
            new_board = self.swap(self.blank_index, self.blank_index - 3)
            tile_value = self.board[self.blank_index - 3]
        elif move == 'down':
            new_board = self.swap(self.blank_index, self.blank_index + 3)
            tile_value = self.board[self.blank_index + 3]
        elif move == 'left':
            new_board = self.swap(self.blank_index, self.blank_index - 1)
            tile_value = self.board[self.blank_index - 1]
        else:
            new_board = self.swap(self.blank_index, self.blank_index + 1)
            tile_value = self.board[self.blank_index + 1]
        return new_board, tile_value
               
    # Swap two tiles
    def swap(self, i, j):
        new_board_array = list(self.board)
        new_board_array[i], new_board_array[j] = new_board_array[j], new_board_array[i]
        return tuple(new_board_array)
        
    # Get children of this node
    def expand_children(self):
        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            child_board, tile_value = self.make_move(move)
            child = Node(
                board=child_board, parent=self, action=move, 
                depth=self.depth+1, path_cost=self.path_cost+tile_value, move_cost=tile_value)
            self.children.append(child)
        self.expanded = True
        
        
        
class searches:
    solution = None
    total_cost = 0
    time = 0
    space = 0
    
    def __init__(self):
        self.solution = []
        
    def display_solution(self):        
        
        for node in self.solution:
            if node.parent:
                print(node.action, ", Cost = ", node.move_cost, ", Path cost = ", node.path_cost)
            node.print_board()
        print("\nSOLUTION\n"
              f"Total cost = {self.total_cost}\n"
              f"Length = {len(self.solution)}\n"
              f"Time = {self.time}\n"
              f"Space = {self.space}\n")         
            
    def bfs(self, root):
        queue = deque()
        visited = set()
        space = 0
        time = 0
        
        queue.append(Node(root))
        
        while len(queue) != 0:
            if len(queue) > self.space: self.space = len(queue) # Space measure
            curr_node = queue.popleft()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): 
                self.total_cost = curr_node.path_cost               
                while curr_node is not None:
                    self.solution.append(curr_node)
                    curr_node = curr_node.parent
                self.solution.reverse()
                self.display_solution()
            else:                
                curr_node.expand_children()
                for child in curr_node.children:
                    if child.board not in visited and child not in queue:
                        queue.append(child)
        return
        
        
    def dfs(self):
        return

    def ucs(self):
        return

    def gbfs(self):
        return

    def a_starS(self):
        return