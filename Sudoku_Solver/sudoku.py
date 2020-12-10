import numpy as py # Use numpy to print in matrix

class Sudoku():

    #Load the grid
    def __init__(self, grid):
        self.grid = grid

    

    # Return true if the value or solution is valid
    def check_Grid(self, y, x, n):
        # Return false if y have the same value
        for i in range(0, 9):
            if self.grid[y][i] == n:
                return False
        # Return false if x have the same value       
        for i in range(0, 9):
            if self.grid[i][x] == n:
                return False

        # Get the box and return false if y, x have the same value
        x_grid = (x // 3) * 3
        y_grid = (y // 3) * 3  
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y_grid + i][x_grid + j] == n:
                    return False

        # Return true if its valid
        return True


    # Solve the Sudoku
    def solveGrid(self):
        
        for y in range(9):
            for x in range(9):
                # Get the y, x and check if the grid have the value of 0
                if self.grid[y][x] == 0:
                    
                    for n in range(1, 10):
                        # if the check_Grid method is true 
                        if self.check_Grid(y,x, n):
                            # insert the value n to grid
                            self.grid[y][x] = n
                            # call the same method until the grid is solve
                            self.solveGrid()
                            # change the grid equals to 0 if its imposible to continue then it will return and try a new value of n
                            self.grid[y][x] = 0

                    return
        
        print(py.matrix(self.grid))
