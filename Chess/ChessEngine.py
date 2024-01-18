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

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--" # when you move a piece the starting square becomes empty
        self.board[move.endRow][move.endCol] = move.pieceMoved # the square where the piece is moved to is now occupied
        self.moveLog.append(move) # log move to display / undo
        self.whiteToMove = not self.whiteToMove # swap players

class Move():
    #map keys to values
    # key : value
    rankToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                  "5": 3, "6": 2, "7": 1, "8":0}
    rowsToRanks = {v: k for k, v in rankToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    
    def getChessNotation(self):
        # can add to make this more like proper chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

        


