"""
This class is responsible for storing all the information about the current state of a chess game. 
Will also be responsible for determing the valid moves at the current state
It will also have a move log
"""

class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 2 characters
        # the first character represents the color
        # second character represents the type piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],

        ]

        self.whiteToMove = True
        self.moveLog = []

class Move():

    def __init__(self, startSq, endSq, board)
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        

        


