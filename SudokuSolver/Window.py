from tkinter import *

class Window:
    """Window of the application"""

    def __init__ (self, title, width, sudoku):
        """Initializes the window"""
        #widgets creation
        self.tkWindow = Tk()
        self.sudoku = sudoku
        self.MAX = 9
        self.loadButton = Button(self.tkWindow, text = "Load Sudoku", command = self.loadSudoku)
        self.startButton = Button(self.tkWindow, text = "Start",  state = DISABLED, command = self.startSolving)
        self.quitButton = Button(self.tkWindow, text=  "Quit", command = self.tkWindow.destroy)
        self.canvasSize = width
        self.canvas =  Canvas(self.tkWindow, bg='white', height = self.canvasSize, width = self.canvasSize)
        

        #widgets configuration
        self.tkWindow.title(title)
        self.tkWindow.resizable(width = FALSE, height = FALSE)
        self.tkWindow.minsize(width = width, height= width + 40)

        #widgets positionnement
        self.canvas.grid(row = 1, columnspan = 4)
        self.loadButton.grid(row = 2, column = 1, padx = 3, pady = 3)
        self.startButton.grid(row = 2, column = 2, padx = 3, pady = 3)
        self.quitButton.grid(row = 2, column = 3, padx = 3, pady = 3)

        #photos
        self.imagesReferences = {}

        #self.imagesReferences[0] = PhotoImage("Ressources/0.png")
        #self.imagesReferences[1] = PhotoImage("Ressources/1.png")
        #self.image = PhotoImage("Ressources/1.png")
        #self.test = None
        #photo = PhotoImage(file = 'C:/SudokuTemp/Ressources/1.png')
        #self.canvas.create_image(0,0, image=photo)
        
        self.updateCanvas()

    def loadSudoku(self):
        """Load sudoku content"""
        self.sudoku.loadContent()
        self.loadButton.config(state = DISABLED)
        self.startButton.config(state = NORMAL)
        self.updateCanvas()

    def startSolving (self):
        """Launch the solving process"""
        self.sudoku.solve()
        self.updateCanvas()
        
    def updateCanvas (self):
        """Prints the sudoku matrix"""
        x = 0
        y = 0
        self.canvas.delete(all)
        #images
        #for i in range(self.MAX):
        #    for j in range(self.MAX):
        #        #photo = PhotoImage(file = "Ressources/1.png")
        #        #self.imagesReferences[i,j] = self.canvas.create_image(x, y, image = photo) # % SUDO[i,j]))
        #        #print(self.imagesReferences[i,j])
        #        print(self.sudoku.matrix[i, j])
        #        x=x+(self.canvasSize/self.MAX)
        #        if x%self.canvasSize == 0:
        #            x=0
        #            y=y+(self.canvasSize/self.MAX)
        #self.test = self.canvas.create_image(10, 10, image = self.image)
        print("\n\n\n\n")
        for i in range(self.MAX):
            print("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t" %(self.sudoku.matrix[i, 0], self.sudoku.matrix[i, 1], self.sudoku.matrix[i, 2],
                                                               self.sudoku.matrix[i, 3], self.sudoku.matrix[i, 4], self.sudoku.matrix[i ,5], 
                                                               self.sudoku.matrix[i, 6], self.sudoku.matrix[i, 7], self.sudoku.matrix[i, 8]))
        #separators
        for i in range(self.MAX):
            dash=i*self.canvasSize/self.MAX
            if(i%3 == 0):
                self.canvas.create_line(dash, 0, dash, self.canvasSize, fill ='black', width = 3)
                self.canvas.create_line(0, dash, self.canvasSize, dash, fill ='black', width = 3)
            else:
                self.canvas.create_line(dash, 0, dash, self.canvasSize, fill ='black', width = 1)
                self.canvas.create_line(0, dash, self.canvasSize, dash, fill ='black', width = 1)