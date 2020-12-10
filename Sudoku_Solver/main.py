import sudoku

# You can change this 2d array values to any sudoku problem
sudoku_grid = [
    [0,0,1,0,0,3,0,0,0],
    [0,0,0,8,5,0,0,0,0],
    [0,4,0,0,2,6,8,0,0],
    [0,7,9,0,0,5,0,0,2],
    [0,0,2,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,2,7],
    [6,0,0,0,4,0,0,0,0],
    [0,0,0,1,9,0,6,8,0]
]


def sudo():
    # call the sudoku class
    sud = sudoku.Sudoku(sudoku_grid)
    sud.solveGrid()
    


        
if __name__ == "__main__":
    sudo()
