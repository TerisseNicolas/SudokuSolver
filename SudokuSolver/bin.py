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
            