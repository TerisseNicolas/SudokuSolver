from tkinter import *

class Window:
    """Window of the application"""

    def __init__ (self, title, width, sudoku):
        """Initializes the window"""
        #widgets creation
        self.tkWindow = Tk()
        self.sudoku = sudoku
        self.MAX = 9
        self.processing = False
        self.loadButton = Button(self.tkWindow, text = "Load Sudoku", command = self.loadSudoku)
        self.startButton = Button(self.tkWindow, text = "Start",  state = DISABLED, command = self.start)
        self.stopButton = Button(self.tkWindow, text = "Stop", state = DISABLED, command = self.stop)
        self.quitButton = Button(self.tkWindow, text=  "Quit", command = self.tkWindow.destroy)
        self.canvasSize = width
        self.canvas =  Canvas(self.tkWindow, bg='white', height = self.canvasSize, width = self.canvasSize)        

        #widgets configuration
        self.tkWindow.title(title)
        self.tkWindow.resizable(width = FALSE, height = FALSE)
        self.tkWindow.minsize(width = width, height= width + 40)

        #widgets positionnement
        self.canvas.grid(row = 1, columnspan = 4)
        self.loadButton.grid(row = 2, column = 0, padx = 3, pady = 3)
        self.startButton.grid(row = 2, column = 1, padx = 3, pady = 3)
        self.stopButton.grid(row = 2, column = 2, padx = 3, pady = 3)
        self.quitButton.grid(row = 2, column = 3, padx = 3, pady = 3)

        #photos
        self.photo = []
        self.photo.append(PhotoImage(file = "Ressources/0.png"))
        self.photo.append(PhotoImage(file = "Ressources/1.png"))
        self.photo.append(PhotoImage(file = "Ressources/2.png"))
        self.photo.append(PhotoImage(file = "Ressources/3.png"))
        self.photo.append(PhotoImage(file = "Ressources/4.png"))
        self.photo.append(PhotoImage(file = "Ressources/5.png"))
        self.photo.append(PhotoImage(file = "Ressources/6.png"))
        self.photo.append(PhotoImage(file = "Ressources/7.png"))
        self.photo.append(PhotoImage(file = "Ressources/8.png"))
        self.photo.append(PhotoImage(file = "Ressources/9.png"))
        
        self.updateCanvas(-1, -1)

    def loadSudoku(self):
        """Load sudoku content"""
        self.sudoku.loadContent()
        self.loadButton.config(state = DISABLED)
        self.startButton.config(state = NORMAL)
        self.updateCanvas(-1, -1)

    def start (self):
        """Launch the solving process"""
        self.processing = True
        self.startButton.config(state = DISABLED)
        self.stopButton.config(state = NORMAL)
        self.sudokuSolving()

    def stop (self):
        """Stop the solving process"""
        self.processing = False
        self.loadButton.config(state = NORMAL)
        self.startButton.config(state = NORMAL)
        self.stopButton.config(state = DISABLED)
        self.updateCanvas(-1, -1)

    def sudokuSolving (self):
        """Iteration in the sudoku solving process"""
        if(self.processing):
            (x,y) = self.sudoku.solve()
            if((x,y) != (-1,-1)):
                self.updateCanvas(x, y)
                self.tkWindow.after(1000, self.sudokuSolving)
            else:
                self.stop()
        
    def updateCanvas (self, a, b):
        """Prints the sudoku matrix"""
        self.canvas.delete("all")

        #images
        x = 33.5
        if((a,b) != (-1,-1)):
            unit = self.canvasSize/self.MAX
            self.canvas.create_rectangle(b*unit, a*unit, 67 + b*unit, 67 + a*unit, fill = "red")
            print("[%d][%d] = %d" % (a, b, self.sudoku.matrix[a,b]))
        for i in range(self.MAX):
            y = 33.5
            for j in range(self.MAX):
                self.canvas.create_image(x, y, image = self.photo[self.sudoku.matrix[j, i]])
                y = y + (self.canvasSize/self.MAX)
            x = x + (self.canvasSize/self.MAX)

        #separators
        for i in range(self.MAX):
            dash=i*self.canvasSize/self.MAX
            if(i%3 == 0):
                self.canvas.create_line(dash, 0, dash, self.canvasSize, fill ='black', width = 3)
                self.canvas.create_line(0, dash, self.canvasSize, dash, fill ='black', width = 3)
            else:
                self.canvas.create_line(dash, 0, dash, self.canvasSize, fill ='black', width = 1)
                self.canvas.create_line(0, dash, self.canvasSize, dash, fill ='black', width = 1)