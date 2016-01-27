# LIBRAIRIES
from Sudoku import *
from Window import *

# GLOBAL
SUDOCANVASSIZE = 600

def main():
    sudoku = Sudoku()
    window = Window("SudokuSolver", SUDOCANVASSIZE, sudoku)

if __name__ == '__main__':
    main()
