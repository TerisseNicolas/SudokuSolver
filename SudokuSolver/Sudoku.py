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
        #self.randomContent()
        self.loadContent()
    def randomContent (self):
        for i in range(9):
            for j in range(9):
                randomf = random.choice(range(100)) % 10
                self.matrix[i,j] = randomf
    def clearContent (self):
        """Empty all frames of the sudoku"""
        for i in range(9):
            for j in range(9):
                self.matrix[i,j] = 0
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
        #fillPersoMatrix2(self.matrix)
        fillDefaultMatrix(self.matrix)
        self.emptyFrame = self.emptyFrameNumber()
    def decreaseEmptyFrameNumber (self):
        """Decrease the number of empty frames"""
        self.emptyFrame -= 1
    def solve (self):
        """Return (row,col) couple if an empty frame has been filled, (-1,-1) otherwise"""
        if(self.emptyFrame != 0):
            (x,y) = (-1,-1)
            try:
                assert True == self.validMatrix()
            except AssertionError:
                print ("Matrix not valid anymore")
            else:
                #rows
                for i in range(9):
                    empty = self.numberEmptyFrameRow(i)
                    if(empty == 0):
                        continue
                    if(empty == 1):
                        (x,y) = self.fillOneEmptyFrameRow(i)
                        if((x,y) != (-1,-1)):
                            print("fillOneEmptyFrameRow")
                            return (x,y)
                    else:
                        numbers = self.missingNumberFrameRow(i)
                        if(len(numbers) == 0):
                            return (-1,-1)
                        indexes = self.rowMissingFrame(i)
                        if(len(indexes) != len(numbers)):
                            return (-1,-1)
                        (x,y) = self.fillEmptyFrameRow(i, numbers, indexes)
                        if((x,y) != (-1,-1)):
                            print("fillEmptyFrameRow")
                            return (x,y)
                        if(empty == 2):
                            (x,y) = self.fillTwoEmptyFrameRow(i)
                            if((x,y) != (-1,-1)):
                                print("fillTwoEmptyFrameRow")
                                return (x,y)
                #cols
                for j in range(9):
                    empty = self.numberEmptyFrameCol(j)
                    if(empty == 0):
                        continue
                    if(empty == 1):
                        (x,y) = self.fillOneEmptyFrameCol(j)
                        if((x,y) != (-1,-1)):
                            print("fillOneEmptyFrameCol")
                            return (x,y)
                    else:
                        numbers = self.missingNumberFrameCol(j)
                        if(len(numbers) == 0):
                            return (-1,-1)
                        indexes = self.colMissingFrame(j)
                        if(len(indexes) != len(numbers)):
                            return (-1,-1)
                        (x,y) = self.fillEmptyFrameCol(j, numbers, indexes)
                        if((x,y) != (-1,-1)):
                            print("fillEmptyFrameCol")
                            return (x,y)
                        if(empty == 2):
                            (x,y) = self.fillTwoEmptyFrameCol(j)
                            if((x,y) != (-1,-1)):
                                print("fillTwoEmptyFrameCol")
                                return (x,y)
                #blocks
                for i in range(3):
                    for j in range(3):
                        empty = self.numberEmptyFrameBlock(i*3, j*3)
                        if(empty == 0):
                            continue
                        if(empty == 1):
                            (x,y) = self.fillOneEmptyFrameBlock(i*3, j*3)
                            if((x,y) != (-1,-1)):
                                print("fillOneEmptyFrameBlock")
                                return (x,y)
                        #elif(empty == 2):
                        #    (x,y) = self.fillTwoEmptyFrameBlock(i*3, j*3)
                        #    if((x,y) != (-1,-1)):
                        #        print("fillTwoEmptyFrameBlock")
                        #        return (x,y)
                        else:
                            numbers = self.missingNumberFrameBlock(i*3, j*3)
                            if(len(numbers) == 0):
                                return (-1,-1)
                            indexes = self.blockMissingFrame(i*3, j*3)
                            if(len(indexes) != len(numbers)):
                                return (-1,-1)
                            (x,y) = self.fillEmptyFrameBlock(i*3, j*3, numbers, indexes)
                            if((x,y) != (-1,-1)):
                                print("fillEmptyFrameBlock")
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
    
    def numberEmptyFrameRow (self, row):
        """Return the number of empty frame in the row"""
        count = 0
        for j in range(9):
            if(self.matrix[row, j] == 0):
                count += 1
        return count
    def numberEmptyFrameCol (self, col):
        """Return the number of empty frame in the column"""
        count = 0
        for i in range(9):
            if(self.matrix[i, col] == 0):
                count +=1
        return count
    def numberEmptyFrameBlock (self, row, col):
        """Return the number of empty frame in the block"""
        count = 0
        for i in range(3):
            for j in range(3):
                if(self.matrix[row + i, col + j] == 0):
                    count += 1
        return count

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

    def rowMissingFrame (self, row):
        """Return the list of column indexes of empty frames"""
        indexList = []
        for j in range(9):
            if(self.matrix[row, j] == 0):
                indexList.append(j)
        return indexList
    def colMissingFrame (self, col):
        """Return the list of row indexes of empty frames"""
        indexList = []
        for i in range(9):
            if(self.matrix[i, col] == 0):
                indexList.append(i)
        return indexList
    def blockMissingFrame (self, row, col):
        """Return the list of position of empty frames"""
        indexList = []
        for i in range(3):
            for j in range(3):
                if(self.matrix[row + i, col + j] == 0):
                    indexList.append((row + i, col + j))
        return indexList

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

    def missingNumberFrameRow (self, row):
        """Return the list of missing numbers of the row"""
        numbers = []
        for k in range(1, 10):
            found = False
            for j in range(9):
                if(self.matrix[row, j] == k):
                    found = True
            if(not found):
                numbers.append(k)
        return numbers
    def missingNumberFrameCol (self, col):
        """Return the list of missing numbers in the column"""
        numbers = []
        for k in range(1, 10):
            found = False
            for i in range(9):
                if(self.matrix[i, col] == k):
                    found = True
            if(not found):
                numbers.append(k)
        return numbers
    def missingNumberFrameBlock (self, row, col):
        """Return the list of missing numbers in the block"""
        numbers = []
        for k in range(1, 10):
            found = False
            for i in range(3):
                for j in range(3):
                    if(self.matrix[row + i, col + j] == k):
                        found = True
            if(not found):
                numbers.append(k)
        return numbers

    # =======================================================================================
    # Filling Functions =====================================================================
    # =======================================================================================

    # OneEmptyFrame Functions ===============================================================
    def fillOneEmptyFrameRow (self, row):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        emptyFrameColIndex = self.rowOneMissingFrame(row)
        if(emptyFrameColIndex == -1):
            return (-1,-1)
        missingNumber = self.missingNumberOneEmptyFrameRow(row)
        if(missingNumber == 0):
            return (-1,-1)
        self.matrix[row, emptyFrameColIndex] = missingNumber
        return (row, emptyFrameColIndex)
    def fillOneEmptyFrameCol (self, col):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        emptyFrameRowIndex = self.colOneMissingFrame(col)
        if(emptyFrameRowIndex == -1):
            return (-1,-1)
        missingNumber = self.missingNumberOneEmptyFrameCol(col)
        if(missingNumber == 0):
            return (-1,-1)
        self.matrix[emptyFrameRowIndex, col] = missingNumber
        return (emptyFrameRowIndex, col)
    def fillOneEmptyFrameBlock (self, row, col):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        emptyFrameBlockIndex = self.blockOneMissingFrame(row, col)
        if(emptyFrameBlockIndex == (-1,-1)):
            return (-1,-1)
        missingNumber = self.missingNumberOneEmptyFrameBlock(row, col)
        if(missingNumber == 0):
            return (-1,-1)
        self.matrix[emptyFrameBlockIndex[0], emptyFrameBlockIndex[1]] = missingNumber
        return emptyFrameBlockIndex   
    
    # TwoEmptyFrame Functions ===============================================================
    def fillTwoEmptyFrameRow(self, row):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        numbers = self.missingNumberFrameRow(row)
        if(len(numbers) != 2):
            return (-1,-1)
        indexes = self.rowMissingFrame(row)
        if(len(indexes) != 2):
            return (-1,-1)
        #Specific Move One
        #block1 = (row - row % 3, indexes[0] - indexes[0] % 3)
        #block2 = (row - row % 3, indexes[1] - indexes[1] % 3)
        #if(self.inBlock(block1[0], block1[1], numbers[0]) != (-1,-1)):
        #    self.matrix[row, indexes[1]] = numbers[0]
        #    return (row,indexes[1])
        #if(self.inBlock(block2[0], block2[1], numbers[0]) != (-1,-1)):
        #    self.matrix[row, indexes[0]] = numbers[0]
        #    return (row,indexes[0])
        #if(self.inBlock(block1[0], block1[1], numbers[1]) != (-1,-1)):
        #    self.matrix[row, indexes[1]] = numbers[1]
        #    return (row,indexes[1])
        #if(self.inBlock(block2[0], block2[1], numbers[1]) != (-1,-1)):
        #    self.matrix[row, indexes[0]] = numbers[1]
        #    return (row,indexes[0])
        return (-1,-1)
    def fillTwoEmptyFrameCol(self, col):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        numbers = self.missingNumberFrameCol(col)
        if(len(numbers) != 2):
            return (-1,-1)
        indexes = self.colMissingFrame(col)
        if(len(indexes) != len(numbers)):
            return (-1,-1)
        #Specific Move One
        #block1 = (col - col % 3, indexes[0] - indexes[0] % 3)
        #block2 = (col - col % 3, indexes[1] - indexes[1] % 3)
        #print("block")
        #print(block1)
        #print(block2)
        #print("numbers")
        #print(numbers)
        #print("indexes")
        #print(indexes)
        #if(self.inBlock(block1[0], block1[1], numbers[0]) != (-1,-1)):
        #    print("case1")
        #    print(self.inBlock(block1[0], block1[1], numbers[0]))
        #    self.matrix[indexes[1], col] = numbers[0]
        #    return (indexes[1],col)
        #if(self.inBlock(block2[0], block2[1], numbers[0]) != (-1,-1)):
        #    print("case2")
        #    self.matrix[indexes[0], col] = numbers[0]
        #    return (indexes[0],col)
        #if(self.inBlock(block1[0], block1[1], numbers[1]) != (-1,-1)):
        #    print("case3")
        #    self.matrix[indexes[1], col] = numbers[1]
        #    return (indexes[1],col)
        #if(self.inBlock(block2[0], block2[1], numbers[1]) != (-1,-1)):
        #    print("case4")
        #    self.matrix[indexes[0], col] = numbers[1]
        #    return (indexes[0],col)
        return (-1,-1)    
    def fillTwoEmptyFrameBlock(self, row, col):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        numbers = self.missingNumberFrameBlock(row, col)
        if(len(numbers) == 0):
            return (-1,-1)
        indexes = self.blockMissingFrame(row, col)
        if(len(indexes) != len(numbers)):
            return (-1,-1)
        #Specific Move One
        #None
        return (-1,-1)
        
    #EmptyFrame Functions ===================================================================
    def fillEmptyFrameRow(self, row, numbers, indexes):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        #MoveOne
        for n in numbers:
            possibility = 0
            possibilityIndex = -1
            for j in indexes:
                if(self.inColumn(j, n) == -1):
                    possibility += 1
                    possibilityIndex = j
            if((possibility) == 1 and (self.inBlock(row - row % 3, possibilityIndex - possibilityIndex % 3, n) == (-1,-1))):
                self.matrix[row, possibilityIndex] = n
                return (row, possibilityIndex)
        return (-1,-1)
    def fillEmptyFrameCol(self, col, numbers, indexes):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        #MoveOne
        for n in numbers:
            possibility = 0
            possibilityIndex = -1
            for i in indexes:
                if(self.inRow(i, n) == -1):
                    possibility += 1
                    possibilityIndex = i
            if((possibility) == 1 and (self.inBlock(possibilityIndex - possibilityIndex % 3, col - col % 3, n) == (-1,-1))):
                self.matrix[possibilityIndex, col] = n
                return (possibilityIndex, col)
        return (-1,-1)
    def fillEmptyFrameBlock(self, row, col, numbers, indexes):
        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
        #MoveOne
        for n in numbers:
            possibility = 0
            possibilityIndex = (-1,-1)
            for (i,j) in indexes:
                if((self.inRow(i, n) == -1 ) and (self.inColumn(j, n) == -1)):
                    possibility += 1
                    possibilityIndex = (i,j)
            if(possibility == 1):
                self.matrix[possibilityIndex[0],possibilityIndex[1]] = n
                return (possibilityIndex[0],possibilityIndex[1])
        return (-1,-1)