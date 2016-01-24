from tkinter import *
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
                #randomf = random.choice(range(100)) % 10
                self.matrix[i,j] = 0 #randomf
    
    def loadContent (self):
        """Loads sudoku data"""
        for i in range(self.MAX):
            for j in range(self.MAX):
                randomf = random.choice(range(100)) % 10
                self.matrix[i,j] = randomf