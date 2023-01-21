import numpy as np

    
class node:
    board = None
    depth = 0
    action = None
    parent = None
    children = None
    pathCost = 0
    expanded = False
    blankIndex = 0    
    
    def __init__(self, board, parent=None, children=None, depth=0, pathCost=0, action=None, expanded=False):
        self.board = board
        self.depth = depth
        self.parent = parent
        self.action = action
        self.children = children
        self.pathCost = pathCost
        self.expanded = expanded
        self.blankIndex = self.board.index(0)
        
    def printBoard(self):
        print(self.board)
                
    def updateBlankIndex(self):
        self.blankIndex = self.board.index(0)
     
    # Moves blank index if valid
    def move(self, move):                
        # If move is valid, swap tiles                  
        if self.isValidMove(move):
            if move == 'up':
                self.swap(self.blankIndex, self.blankIndex - 3)
            elif move == 'down':
                self.swap(self.blankIndex, self.blankIndex + 3)
            elif move == 'left':
                self.swap(self.blankIndex, self.blankIndex - 1)
            else:
                self.swap(self.blankIndex, self.blankIndex + 1)
        else:
            print("'{move}' is not a valid move")
           
    # Checks is given move is valid based on index of blank tile
    def isValidMove(self, move) -> bool:    
        index = self.board.index(0)
        row = np.floor(index / 3)
        col = index % 3    
        
        if row == 0:
            if col == 0:
                possibleMoves = ["right", "down"]
            elif col == 1:                
                possibleMoves = ["right", "left", "down"]
            else:
                possibleMoves = ["left", "down"]                
        elif row == 1:
            if col == 0:
                possibleMoves = ["up", "right", "down"]
            elif col == 1:
                possibleMoves = ["up", "right", "left", "down"]
            else:
                possibleMoves = ["up", "left", "down"]
        else:
            if col == 0:
                possibleMoves = ["up", "right"]
            elif col == 1:
                possibleMoves = ["up", "right", "left"]
            else:
                possibleMoves = ["up", "left"]        
        return move in possibleMoves     
     
    # Swap two tiles                           
    def swap(self, i, j):
        new_board = self.board.copy()
        new_board[i], new_board[j] = new_board[j], new_board[i]
        self.board = new_board
        self.updateBlankIndex()