from tkinter import *
from init_test import *
import random


class Sudoku:
    """Sudoku class"""

    def __init__ (self):
        """Initializes the sudoku"""
        self.isComplet = False
        self.matrix = {}
        self.MAX = 9
        
        for i in range(self.MAX):
            for j in range(self.MAX):
                randomf = random.choice(range(100)) % 10
                self.matrix[i,j] = randomf
    
    def loadContent (self):
        """Loads sudoku data"""
        #for i in range(self.MAX):
        #    for j in range(self.MAX):
        #        randomf = random.choice(range(100)) % 10
        #        self.matrix[i,j] = randomf

        #fillDefaultMatrix(self.matrix)
        fillPersoMatrix(self.matrix)

    # =======================================================================================
    # Explore Functions ======================================================================
    # =======================================================================================

    def inRow (self, row, number):
        """Return -1 if not present, the column index otherwise"""
        for j in range(self.MAX):
            if (self.matix[row,j] == number):
                return j
        return -1

    def inColumn (self, col, number):
        """Return -1 if not present, the row index otherwise"""
        for i in range(self.MAX):
            if(self.matrix[i,col] == number):
                return i
        return -1

    def inBlock (self, row, col, number):
        """Return (-1,-1) if not present, the position couple otherwise"""
        for i in range (row, row+3):
            for j in range (col, col+3):
                if(self.matrix[i,j] == number):
                    return (i,j)
        return (-1,-1)

    def rowOneMissingFrame (self, row):
        """Return 1 if only one frame is missing, 0 otherwise"""
        count = 0
        for j in range(self.MAX):
            if(self.matrix[row,j] == 0):
                count +=1
        return count == 1
    
    def colOneMissingFrame (self, col):
        """Return 1 if only one frame is missing, 0 otherwise"""
        count = 0
        for i in range(self.MAX):
            if(self.matrix[i, col] == 0):
                count +=1
        return count == 1