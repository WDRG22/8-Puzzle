import numpy as np

    
class Node:
    board = []
    depth = 0
    action = None
    parent = None
    children = []
    path_cost = 0
    expanded = False
    
    def __init__(self, board, parent=None, children=[], depth=0, path_cost=0, action=None, expanded=False):
        self.board = board
        self.depth = depth
        self.parent = parent
        self.action = action
        self.children = children
        self.path_cost = path_cost
        self.expanded = expanded
        self.blank_index = self.board.index(0)
        
    def print_board(self):
        print(self.board)

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
        possible_moves = self.get_possible_moves
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
        new_board = self.board.copy()
        new_board[i], new_board[j] = new_board[j], new_board[i]
        return new_board
        
    def expand_children(self):
        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            child_board, tile_value = self.make_move(move)
            child = Node(
                board=child_board, parent=self, action=move, 
                depth=self.depth+1, path_cost=self.path_cost+tile_value)
            self.children.append(child)
        self.expanded = True