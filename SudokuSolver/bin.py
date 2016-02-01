# def solve2(self):
#        """Return (row,col) couple if an emptyFrame has been filled, (-1,-1) otherwise"""
#        if(self.emptyFrame != 0):
#            (x,y) = (-1,-1)
#            try:
#                assert True == self.validMatrix()
#            except AssertionError:
#                print ("Matrix not valid anymore")
#            else:
#                (x, y) = self.oneEmptyFrameStrategy()
#                if((x, y) != (-1, -1)):
#                    print("oneEmptyFrameStrategy")
#                    self.decreaseEmptyFrameNumber()
#                    return (x,y)
#                (x,y) = self.twoEmptyFrameStrategyMoveOne() ## pb avec le 4 !!
#                if((x, y) != (-1, -1)):
#                    print("twoEmptyFrameStrategyMoveOne")
#                    self.decreaseEmptyFrameNumber()
#                    return (x,y)
#                (x,y) = self.twoEmptyFrameStrategyMoveTwo()
#                if((x, y) != (-1, -1)):
#                    print("twoEmptyFrameStrategyMoveTwo")
#                    self.decreaseEmptyFrameNumber()
#                    return (x,y)
#            return (-1,-1)
#        else:
#            return (-1,-1)


## TwoEmptyFrameStrategyMoveOne Functions ================================================
#    def fillTwoEmptyFrameRowStrategyMoveOne(self, row, col1, col2):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
#        if((number1,number2) == (0,0)):
#            return (-1,-1)
#        if(self.inColumn(col1, number1)):
#            print("in")
#            print("col %d number %d" % (col1, number1))
#            self.matrix[row, col2] = number1
#            return (row,col2)
#        if(self.inColumn(col2, number1)):
#            self.matrix[row, col1] = number1
#            return(row,col1)
#        if(self.inColumn(col1, number2)):
#            self.matrix[row, col2] = number2
#            return (row, col2)
#        if(self.inColumn(col2, number2)):
#            self.matrix[row,col1] = number2
#            return (row,col2)
#        return (-1,-1)
#    def fillTwoEmptyFrameColStrategyMoveOne(self, col, row1, row2):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
#        if((number1,number2) == (-1,-1)):
#            retrun (-1,-1)
#        if(self.inRow(row1, number1)):
#            self.matrix[row2, col] = number1
#            return (row2, col)
#        if(self.inRow(row2, number1)):
#            self.matrix[row1, col] = number1
#            return (row1,col)
#        if(self.inRow(row1, number2)):
#            self.matrix[row2, col] = number2
#            return (row2,col)
#        if(self.inRow(row2, number2)):
#            self.matrix[row1, col] = number2
#            return (row1,col)
#        return (-1,-1)


#    # TwoEmptyFrameStrategyMoveTwo Functions ================================================
#    def fillTwoEmptyFrameRowStrategyMoveTwo(self, row, col1, col2):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
#        if((number1,number2) == (0,0)):
#            return (-1,-1)
#        block1 = (row - row % 3, col1 - col1 % 3)
#        block2 = (row - row % 3, col2 - col2 % 3)
#        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
#            self.matrix[row, col2] = number1
#            return (row,col2)
#        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
#            self.matrix[row, col1] = number1
#            return (row,col1)
#        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
#            self.matrix[row, col2] = number2
#            return (row,col2)
#        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
#            self.matrix[row, col1] = number2
#            return (row,col1)
#        return (-1,-1)


#    def fillTwoEmptyFrameColStrategyMoveTwo(self, col, row1, row2):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
#        if((number1,number2) == (0,0)):
#            return (-1,-1)
#        block1 = (col - col % 3, row1 - row1 % 3)
#        block2 = (col - col % 3, row2 - row2 % 3)
#        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
#            self.matrix[row2, col] = number1
#            return (row2,col)
#        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
#            self.matrix[row1, col] = number1
#            return (row1,col)
#        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
#            self.matrix[row2, col] = number2
#            return (row2,col)
#        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
#            self.matrix[row1, col] = number2
#            return (row1,col)
#        return (-1,-1)

#def oneEmptyFrameStrategy (self):
#        """Return the (row,col) position of the filled frame, (-1,-1) otherwise""" 
#        for i in range (9):
#            col = self.rowOneMissingFrame(i)
#            if(col != -1):
#                try:
#                    assert col == self.fillOneEmptyFrameRow(i)
#                except AssertionError:
#                    print("OneEmptyFrameStrategyError : row")
#                else:
#                    return (i, col)
#        for j in range (9):
#            row = self.colOneMissingFrame(j)
#            if(row != -1):
#                try:
#                    assert row == self.fillOneEmptyFrameCol(j)
#                except AssertionError:
#                    print("OneEmptyFrameStrategyError : col")
#                else:
#                    return (row, j)
#        for i in range (3):
#            for j in range(3):
#                row, col = self.blockOneMissingFrame(i*3, j*3)
#                if((row,col) != (-1,-1)):
#                    try:
#                        assert (row,col) == self.fillOneEmptyFrameBlock(i, j)
#                    except AssertionError:
#                        print("OneEmptyFrameStrategyError : block")
#                    else:
#                        return (row, col)
#        return (-1,-1)
#    def twoEmptyFrameStrategyMoveOne (self):
#        """Return the (row,col) position of the filled frame, (-1,-1) otherwise"""
#        for i in range(9):
#            (col1,col2) = self.rowTwoMissingFrame(i)
#            if((col1,col2) != (-1,-1)):
#                (row,col) = self.fillTwoEmptyFrameRowStrategyMoveOne(i, col1, col2)
#                if((row,col) != (-1,-1)):
#                    return (row,col)
#        for j in range(9):
#            (row1,row2) = self.colTwoMissingFrame(j)
#            if((row1,row2) != (-1,-1)):
#                (row,col) = self.fillTwoEmptyFrameColStrategyMoveOne(j, row1, row2)
#                if((row,col) != (-1,-1)):
#                    return (row,col)
#        return (-1,-1)
#    def twoEmptyFrameStrategyMoveTwo (self):
#        """Return the (row,col) position of the filled frame, (-1,-1) otherwise"""
#        for i in range(9):
#            (col1,col2) = self.rowTwoMissingFrame(i)
#            if((col1,col2) != (-1,-1) and not self.inSameBlock(col1, col2)):
#                (row,col) = self.fillTwoEmptyFrameRowStrategyMoveTwo(i, col1, col2)
#                if((col,row) != (-1,-1)):
#                    return (row,col)
#        for j in range(9):
#            (row1,row2) = self.colTwoMissingFrame(j)
#            if((row1,row2) != (-1,-1) and not self.inSameBlock(row1, row2)):
#                (row,col) = self.fillTwoEmptyFrameColStrategyMoveTwo(j, row1, row2)
#                if((col,row) != (-1,-1)):
#                    return (row,col)
#        return (-1,-1)



    ## TwoEmptyFrameMoveTwo Functions ================================================
    #def fillTwoEmptyFrameRowMoveTwo(self, row): #, col1, col2):
    #    """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
    #    (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
    #    if((number1,number2) == (0,0)):
    #        return (-1,-1)
    #    (col1,col2) = self.rowTwoMissingFrame(row)
    #    if((col1,col2) != (-1,-1)):
    #        block1 = (row - row % 3, col1 - col1 % 3)
    #        block2 = (row - row % 3, col2 - col2 % 3)
    #        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
    #            self.matrix[row, col2] = number1
    #            return (row,col2)
    #        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
    #            self.matrix[row, col1] = number1
    #            return (row,col1)
    #        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
    #            self.matrix[row, col2] = number2
    #            return (row,col2)
    #        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
    #            self.matrix[row, col1] = number2
    #            return (row,col1)
    #    return (-1,-1)
    #def fillTwoEmptyFrameColMoveTwo(self, col, row1, row2):
    #    """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
    #    (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
    #    if((number1,number2) == (0,0)):
    #        return (-1,-1)
    #    block1 = (col - col % 3, row1 - row1 % 3)
    #    block2 = (col - col % 3, row2 - row2 % 3)
    #    if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
    #        self.matrix[row2, col] = number1
    #        return (row2,col)
    #    if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
    #        self.matrix[row1, col] = number1
    #        return (row1,col)
    #    if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
    #        self.matrix[row2, col] = number2
    #        return (row2,col)
    #    if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
    #        self.matrix[row1, col] = number2
    #        return (row1,col)
    #    return (-1,-1)

#def fillTwoEmptyFrameRowSauv(self, row):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameRow(row)
#        if((number1,number2) == (0,0)):
#            return (-1,-1)
#        (col1,col2) = self.rowTwoMissingFrame(row)
#        if((col1,col2) == (-1,-1)):
#            return (-1,-1)
#        #MoveTwo
#        block1 = (row - row % 3, col1 - col1 % 3)
#        block2 = (row - row % 3, col2 - col2 % 3)
#        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
#            self.matrix[row, col2] = number1
#            return (row,col2)
#        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
#            self.matrix[row, col1] = number1
#            return (row,col1)
#        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
#            self.matrix[row, col2] = number2
#            return (row,col2)
#        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
#            self.matrix[row, col1] = number2
#            return (row,col1)
#        return (-1,-1)
#    def fillTwoEmptyFrameColSauv(self, col):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameCol(col)
#        if((number1,number2) == (-1,-1)):
#            retrun (-1,-1)
#        (row1,row2) = self.colTwoMissingFrame(col)
#        if((row1,row2) == (-1,-1)):
#            return (-1,-1)
#        #MoveTwo
#        block1 = (col - col % 3, row1 - row1 % 3)
#        block2 = (col - col % 3, row2 - row2 % 3)
#        if(self.inBlock(block1[0], block1[1], number1) != (-1,-1)):
#            self.matrix[row2, col] = number1
#            return (row2,col)
#        if(self.inBlock(block2[0], block2[1], number1) != (-1,-1)):
#            self.matrix[row1, col] = number1
#            return (row1,col)
#        if(self.inBlock(block1[0], block1[1], number2) != (-1,-1)):
#            self.matrix[row2, col] = number2
#            return (row2,col)
#        if(self.inBlock(block2[0], block2[1], number2) != (-1,-1)):
#            self.matrix[row1, col] = number2
#            return (row1,col)
#        return (-1,-1)
#    def fillTwoEmptyFrameBlockSauv(self, row, col):
#        """Return the (row,col) of the filled frame, (-1,-1) otherwise"""
#        (number1,number2) = self.missingNumberTwoEmptyFrameBlock(row, col)
#        if((number1,number2) == (0,0)):
#            return (-1,-1)
#        (pos1,pos2) = self.blockTwoMissingFrame(row, col)
#        if((pos1,pos2) == ((-1,-1),(-1,-1))):
#            return (-1,-1)
#        return (-1,-1)

#def missingNumberTwoEmptyFrameRow (self, row):
    #    """Return the two missing numbers of the row"""
    #    number1 = -1
    #    for k in range(1, 10):
    #        found = False
    #        for j in range(9):
    #            if(self.matrix[row, j] == k):
    #                found = True
    #        if (not found):
    #            if(number1 == -1):
    #                number1 = k
    #            else:
    #                return (number1,k)
    #    return (0,0)
    #def missingNumberTwoEmptyFrameCol (self, col):
    #    """Return the two missing numbers of the col"""
    #    number1 = -1
    #    for k in range(1, 10):
    #        found = False
    #        for i in range(9):
    #            if(self.matrix[i, col] == k):
    #                found = True
    #        if (not found):
    #            if(number1 == -1):
    #                number1 = k
    #            else:
    #                return (number1,k)
    #    return (0,0)
    #def missingNumberTwoEmptyFrameBlock (self, row, col):
    #    """Return the missing number of the block"""
    #    number1 = -1
    #    for k in range(1, 10):
    #        found = False
    #        for i in range(3):
    #            for j in range(3):
    #                if(self.matrix[row + i, col + j] == k):
    #                    found = True
    #        if(not found):
    #            if(number1 == -1):
    #                number1 = k
    #            else:
    #                return (number1, k)
    #    return (0,0)

    #def rowTwoMissingFrame (self, row):
    #    """Return the column indexes of the frames if two are missing, (-1,-1) otherwise"""
    #    count = 0
    #    index1 = -1
    #    index2 = -1
    #    for j in range(9):
    #        if(self.matrix[row,j] == 0):
    #            count +=1
    #            if(index1 == -1):
    #                index1 = j
    #            else:
    #                index2 = j
    #    if(count == 2):
    #        return (index1, index2)
    #    else:
    #        return (-1,-1)   
    #def colTwoMissingFrame (self, col):
    #    """Return the row indexes of the frames if two are missing, (-1,-1) otherwise"""
    #    count = 0
    #    index1 = -1
    #    index2 = -1
    #    for i in range(9):
    #        if(self.matrix[i, col] == 0):
    #            count +=1
    #            if(index1 == -1):
    #                index1 = i
    #            else:
    #                index2 = i
    #    if(count == 2):
    #        return (index1, index2)
    #    else:
    #        return (-1,-1)
    #def blockTwoMissingFrame (self, row, col):
    #    """Return the couple ((x1,y1), (x2,y2)) of the missing frames, ((-1,-1), (-1,-1)) otherwise"""
    #    index1 = (-1,-1)
    #    index2 = (-1,-1)
    #    for i in range(3):
    #        for j in range(3):
    #            if(self.matrix[row + i, col + j] == 0):
    #                if(index1 == (-1,-1)):
    #                    index1 = (row+i,col+j)
    #                else:
    #                    index2 = (row+i,col+j)
    #    return (index1,index2)
#def solve2 (self):
#        """Return (row,col) couple if an empty frame has been filled, (-1,-1) otherwise"""
#        if(self.emptyFrame != 0):
#            (x,y) = (-1,-1)
#            try:
#                assert True == self.validMatrix()
#            except AssertionError:
#                print ("Matrix not valid anymore")
#            else:
#                #rows
#                for i in range(9):
#                    empty = self.numberEmptyFrameRow(i)
#                    if(empty == 0):
#                        continue
#                    if(empty == 1):
#                        (x,y) = self.fillOneEmptyFrameRow(i)
#                        if((x,y) != (-1,-1)):
#                            print("fillOneEmptyFrameRow")
#                            return (x,y)
#                    elif(empty == 2):
#                        (x,y) = self.fillTwoEmptyFrameRow(i)
#                        if((x,y) != (-1,-1)):
#                            print("fillTwoEmptyFrameRow")
#                            return (x,y)
#                    else:
#                        (x,y) = self.fillEmptyFrameRow(i)
#                        if((x,y) != (-1,-1)):
#                            print("fillEmptyFrameRow")
#                            return (x,y)
#                #cols
#                for j in range(9):
#                    empty = self.numberEmptyFrameCol(j)
#                    if(empty == 0):
#                        continue
#                    if(empty == 1):
#                        (x,y) = self.fillOneEmptyFrameCol(j)
#                        if((x,y) != (-1,-1)):
#                            print("fillOneEmptyFrameCol")
#                            return (x,y)
#                    elif(empty == 2):
#                        (x,y) = self.fillTwoEmptyFrameCol(j)
#                        if((x,y) != (-1,-1)):
#                            print("fillTwoEmptyFrameCol")
#                            return (x,y)
#                    else:
#                        (x,y) = self.fillEmptyFrameCol(j)
#                        if((x,y) != (-1,-1)):
#                            print("fillEmptyFrameCol")
#                            return (x,y)
#                #blocks
#                for i in range(3):
#                    for j in range(3):
#                        empty = self.numberEmptyFrameBlock(i*3, j*3)
#                        if(empty == 0):
#                            continue
#                        if(empty == 1):
#                            (x,y) = self.fillOneEmptyFrameBlock(i*3, j*3)
#                            if((x,y) != (-1,-1)):
#                                print("fillOneEmptyFrameBlock")
#                                return (x,y)
#                        else:
#                            if(empty == 2):
#                                (x,y) = self.fillTwoEmptyFrameBlock(i*3, j*3)
#                                if((x,y) != (-1,-1)):
#                                    print("fillTwoEmptyFrameBlock")
#                                    return (x,y)
#                            (x,y) = self.fillEmptyFrameBlock(i*3, j*3)
#                            if((x,y) != (-1,-1)):
#                                print("fillEmptyFrameBlock")
#                                return (x,y)
#            return (-1,-1)
#        else:
#            return (-1,-1)