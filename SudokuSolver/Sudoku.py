from tkinter import *
from init_test import *
import random


class Sudoku:
    """Sudoku class"""

    def __init__ (self):
        """Initializes the sudoku"""
        self.isComplet = False
        self.emptyFrame = 0
        self.matrix = {}
        self.randomContent()
    def randomContent (self):
        for i in range(9):
            for j in range(9):
                randomf = random.choice(range(100)) % 10
                self.matrix[i,j] = randomf   
    def loadContent2 (self):
        """Loads sudoku data"""
        #for i in range(9):
        #    for j in range(9):
        #        randomf = random.choice(range(100)) % 10
        #        self.matrix[i,j] = randomf

        #fillDefaultMatrix(self.matrix)
        a = 1
    def loadContent (self):
        """Loads sudoku data"""
        #fillPersoMatrix(self.matrix)
        fillDefaultMatrix(self.matrix)
        self.emptyFrame = self.emptyFrameNumber()
    def decreaseEmptyFrameNumber (self):
        """Decrease the number of empty frames"""
        self.emptyFrame -= 1
    def solve(self):
        """Return (row,col) couple if an emptyFrame has been filled, (-1,-1) otherwise"""
        flag = True
        if(self.emptyFrame != 0):
            (x,y) = (-1,-1)
            try:
                assert True == self.validMatrix()
            except AssertionError:
                print ("Matrix not valid anymore")
            else:
                #(x, y) = self.oneEmptyFrameStrategy()
                #if((x, y) != (-1, -1)):
                #    self.decreaseEmptyFrameNumber()
                #    return (x,y)
                #(x,y) = self.TwoEmptyFrameStrategyMoveOne()
                #if((x, y) != (-1, -1)):
                #    self.decreaseEmptyFrameNumber()
                #    return (x,y)
                (x,y) = self.twoEmptyFrameStrategyMoveTwo()
                if((x, y) != (-1, -1)):
                    self.decreaseEmptyFrameNumber()
                    return (x,y)
            return (-1,-1)
        else:
            return (-1,-1)
    def debug (self):
        """Debuging function"""
        print(self.oneEmptyFrameStrategy())
            
    # =======================================================================================
    # Explore Functions ======================================================================
    # =======================================================================================

    def emptyFrameNumber (self):
        """Return the number of empty frame in the matrix"""
        count = 0
        for i in range (9):
            for j in range(9):
                if(self.matrix[i, j] == 0):
                    count += 1
        return count
    def inRow (self, row, number):
        """Return -1 if not present, the column index otherwise"""
        for j in range(9):
            if (self.matrix[row,j] == number):
                return j
        return -1
    def inColumn (self, col, number):
        """Return -1 if not present, the row index otherwise"""
        for i in range(9):
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
    def inSameBlock (self, index1, index2):
        """Return True if the two indexes are in the same block (for one row or column), False otherwise"""
        a = index1 - index1 % 3
        b = index2 - index2 % 3
        return a == b
    
    def rowOneMissingFrame (self, row):
        """Return the column index of the frame if only one is missing, -1 otherwise"""
        count = 0
        index = -1
        for j in range(9):
            if(self.matrix[row,j] == 0):
                count +=1
                index = j
        if(count == 1):
            return index
        else:
            return -1   
    def colOneMissingFrame (self, col):
        """Return the row index of the frame if only one is missing, -1 otherwise"""
        count = 0
        index = -1
        for i in range(9):
            if(self.matrix[i, col] == 0):
                count +=1
                index = i
        if(count == 1):
            return index
        else:
            return -1
    def blockOneMissingFrame (self, row, col):
        """Return the couple (row,col) index of the frame if only one is missing, (-1,-1) otherwise"""
        count = 0
        index = (-1,-1)
        for i in range (row, row+3):
            for j in range (col, col+3):
                if(self.matrix[i, j] == 0):
                    count += 1
                    index = (i, j)
        if(count == 1):
            return index
        else:
            return (-1,-1)
    
    def rowTwoMissingFrame (self, row):
        """Return the column indexes of the frames if two are missing, (-1,-1) otherwise"""
        count = 0
        index1 = -1
        index2 = -1
        for j in range(9):
            if(self.matrix[row,j] == 0):
                count +=1
                if(index1 == -1):
                    index1 = j
                else:
                    index2 = j
        if(count == 2):
            return (index1, index2)
        else:
            return (-1,-1)   
    def colTwoMissingFrame (self, col):
        """Return the row indexes of the frames if two are missing, (-1,-1) otherwise"""
        count = 0
        index1 = -1
        index2 = -1
        for i in range(9):
            if(self.matrix[i, col] == 0):
                count +=1
                if(index1 == -1):
                    index1 = i
                else:
                    index2 = i
        if(count == 2):
            return (index1, index2)
        else:
            return (-1,-1)   

    # =======================================================================================
    # Validity Functions ====================================================================
    # =======================================================================================

    def validMatrix (self):
        """Return true if the matrix is valid, false otherwise"""
        for i in range(9):
            if(not self.validRow(i)):
                return False
        for j in range(9):
            if(not self.validColumn(j)):
                return False
        for i in range(3):
            for j in range(3):
                if(not self.validBlock(i*3, j*3)):
                    return False
        return True
    def validRow (self, row):
        """Return true if the row is valid, false otherwise"""
        for k in range(1, 10):
            count = 0
            for j in range(9):
                if(self.matrix[row, j] == k):
                    count += 1
            if(count > 1):
                return False
        return True
    def validColumn (self, col):
        """Return true if the column is valid, false otherwise"""
        for k in range(1, 10):
            count = 0
            for i in range(9):
                if(self.matrix[i, col] == k):
                    count += 1
            if(count > 1):
                return False
        return True
    def validBlock (self, row, col):
        """Return true if the bloc is valid, false otherwise"""
        for k in range(1, 10):
            count = 0
            for i in range(3):
                for j in range(3):
                    if(self.matrix[row + i, col + j] == k):
                        count += 1
            if(count > 1):
                return False
        return True

    # =======================================================================================
    # Access Functions ======================================================================
    # =======================================================================================
    
    def missingNumberOneEmptyFrameRow (self, row):
        """Return the missing number of the row"""
        for k in range(1, 10):
            found = False
            for j in range(9):
                if(self.matrix[row, j] == k):
                    found = True
            if (not found):
                return k
        return 0
    def missingNumberOneEmptyFrameCol (self, col):
        """Return the missing number of the col"""
        for k in range(1, 10):
            found = False
            for i in range(9):
                if(self.matrix[i, col] == k):
                    found = True
            if (not found):
                return k
        return 0
    def missingNumberOneEmptyFrameBlock (self, row, col):
        """Return the missing number of the row"""
        for k in range(1, 10):
            found = False
            for i in range(3):
                for j in range(3):
                    if(self.matrix[row + i, col + j] == k):
                        found = True
            if (not found):
                return k
        return 0
    
    def missingNumberTwoEmptyFrameRow (self, row):
        """Return the two missing numbers of the row"""
        number1 = -1
        for k in range(1, 10):
            found = False
            for j in range(9):
                if(self.matrix[row, j] == k):
                    found = True
            if (not found):
                if(number1 == -1):
                    number1 = k
                else:
                    return (number1,k)
        return (0,0)
    def missingNumberTwoEmptyFrameCol (self, col):
        """Return the two missing numbers of the col"""
        number1 = -1
        for k in range(1, 10):
            found = False
            for i in range(9):
                if(self.matrix[i, col] == k):
                    found = True
            if (not found):
                if(number1 == -1):
                    number1 = k
                else:
                    return (number1,k)
        return (0,0)

    # =======================================================================================
    # Strategies Functions ==================================================================
    # =======================================================================================

    def oneEmptyFrameStrategy (self):
        """Return the (row,col) position of the filled frame, (-1,-1) otherwise""" 
        for i in range (9):
            col = self.rowOneMissingFrame(i)
            if(col != -1):
                try:
                    assert col == self.fillOneEmptyFrameRow(i)
                except AssertionError:
                    print("OneEmptyFrameStrategyError : row")
                else:
                    return (i, col)
        for j in range (9):
            row = self.colOneMissingFrame(j)
            if(row != -1):
                try:
                    assert row == self.fillOneEmptyFrameCol(j)
                except AssertionError:
                    print("OneEmptyFrameStrategyError : col")
                else:
                    return (row, j)
        for i in range (3):
            for j in range(3):
                row, col = self.blockOneMissingFrame(i*3, j*3)
                if((row,col) != (-1,-1)):
                    try:
                        assert (row,col) == self.fillOneEmptyFrameBlock(i, j)
                    except AssertionError:
                        print("OneEmptyFrameStrategyError : block")
                    else:
                        return (row, col)
        return (-1,-1)
    def twoEmptyFrameStrategyMoveOne (self):
        """Return the (row,col) position of the filled frame, (-1,-1) otherwise"""
        for i in range(9):
            (col1,col2) = self.rowTwoMissingFrame(i)
            if((col1,col2) != (-1,-1)):
                (row,col) = self.fillTwoEmptyFrameRowStrategyMoveOne(i, col1, col2)
                if((row,col) != (-1,-1)):
                    return (row,col)
        for j in range(9):
            (row1,row2) = self.colTwoMissingFrame(j)
            if((row1,row2) != (-1,-1)):
                (row,col) = self.fillTwoEmptyFrameColStrategyMoveOne(j, row1, row2)
                if((row,col) != (-1,-1)):
                    return (row,col)
        return (-1,-1)
    def twoEmptyFrameStrategyMoveTwo (self):
        """Return the (row,col) position of the filled frame, (-1,-1) otherwise"""
        for i in range(9):
            (col1,col2) = self.rowTwoMissingFrame(i)
            if((col1,col2) != (-1,-1) and not self.inSameBlock(col1, col2)):
                (row,col) = self.fillTwoEmptyFrameRowStrategyMoveTwo(i, col1, col2)
                if((col,row) != (-1,-1)):
                    return (row,col)
        for j in range(9):
            (row1,row2) = self.colTwoMissingFrame(j)
            if((row1,row2) != (-1,-1) and not self.inSameBlock(row1, row2)):
                (row,col) = self.fillTwoEmptyFrameColStrategyMoveTwo(j, row1, row2)
                if((col,row) != (-1,-1)):
                    return (row,col)
        return (-1,-1)
            
    # OneEmptyFrameStrategy Functions =======================================================
    def fillOneEmptyFrameRow (self, row):
        """Fill the empty frame of the row, return the col index if succeed, -1 otherwise"""
        emptyFrameColIndex = self.rowOneMissingFrame(row)
        if(emptyFrameColIndex == -1):
            return -1
        missingNumber = self.missingNumberOneEmptyFrameRow(row)
        if(missingNumber == 0):
            return -1
        self.matrix[row, emptyFrameColIndex] = missingNumber
        return emptyFrameColIndex
    def fillOneEmptyFrameCol (self, col):
        """Fill the empty frame of the col, return the row index if succeed, -1 otherwise"""
        emptyFrameRowIndex = self.colOneMissingFrame(col)
        if(emptyFrameRowIndex == -1):
            return -1
        missingNumber = self.missingNumberOneEmptyFrameCol(col)
        if(missingNumber == 0):
            return -1
        self.matrix[emptyFrameRowIndex, col] = missingNumber
        return emptyFrameRowIndex
    def fillOneEmptyFrameBlock (self, row, col):
        """Fill the empty frame of the block, return the (row,col) index if succeed, (-1,-1) otherwise"""
        emptyFrameBlockIndex = self.blockOneMissingFrame(row, col)
        if(emptyFrameBlockIndex == (-1,-1)):
            return -1
        missingNumber = self.missingNumberOneEmptyFrameBlock(row, col)
        if(missingNumber == 0):
            return -1
        self.matrix[emptyFrameBlockIndex[0], emptyFrameBlockIndex[1]] = missingNumber
        return emptyFrameBlockIndex   
    
    # TwoEmptyFrameStrategyMoveOne Functions ================================================
    def fillTwoEmptyFrameRowStrategyMoveOne(self, row, col1, col2):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
        if((number1,number2) == (0,0)):
            return (-1,-1)
        if(self.inColumn(col1, number1)):
            self.matrix[row, col2] = number1
            return (row,col2)
        if(self.inColumn(col2, number1)):
            self.matrix[row, col1] = number1
            return(row,col1)
        if(self.inColumn(col1, number2)):
            self.matrix[row, col2] = number2
            return (row, col2)
        if(self.inColumn(col2, number2)):
            self.matrix[row,col1] = number2
            return (row,col2)
        return (-1,-1)
    def fillTwoEmptyFrameColStrategyMoveOne(self, col, row1, row2):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
        if((number1,number2) == (-1,-1)):
            retrun (-1,-1)
        if(self.inRow(row1, number1)):
            self.matrix[row2, col] = number1
            return (row2, col)
        if(self.inRow(row2, number1)):
            self.matrix[row1, col] = number1
            return (row1,col)
        if(self.inRow(row1, number2)):
            self.matrix[row2, col] = number2
            return (row2,col)
        if(self.inRow(row2, number2)):
            self.matrix[row1, col] = number2
            return (row1,col)
        return (-1,-1)

    # TwoEmptyFrameStrategyMoveTwo Functions ================================================
    def fillTwoEmptyFrameRowStrategyMoveTwo(self, row, col1, col2):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
        if((number1,number2) == (0,0)):
            return (-1,-1)
        block1 = (row - row % 3, col1 - col1 % 3)
        block2 = (row - row % 3, col2 - col2 % 3)
        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
            self.matrix[row, col2] = number1
            return (row,col2)
        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
            self.matrix[row, col1] = number1
            return (row,col1)
        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
            self.matrix[row, col2] = number2
            return (row,col2)
        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
            self.matrix[row, col1] = number2
            return (row,col1)
        return (-1,-1)
    def fillTwoEmptyFrameColStrategyMoveTwo(self, col, row1, row2):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
        if((number1,number2) == (0,0)):
            return (-1,-1)
        block1 = (col - col % 3, row1 - row1 % 3)
        block2 = (col - col % 3, row2 - row2 % 3)
        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
            self.matrix[row2, col] = number1
            return (row2,col)
        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
            self.matrix[row1, col] = number1
            return (row1,col)
        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
            self.matrix[row2, col] = number2
            return (row2,col)
        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
            self.matrix[row1, col] = number2
            return (row1,col)
        return (-1,-1)