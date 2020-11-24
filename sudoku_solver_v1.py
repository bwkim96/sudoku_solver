# Version 1 of Sudoku Solver: simple text-based sudoku solver

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# function to print the board to command line
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(len(board[i])):
            if j % 3 == 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print("|")
    print("-------------------------")

# function to find the next empty cell in the board, return a tuple (row, column)
def next_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)

# function to check if the input number at input position is a valid number
def check_valid(board, num, row, col):
    # check the row
    for i in range (len(board[0])):
        if board[row][i] == num:
            return False
    # check the column
    for i in range (len(board)):
        if board[i][col] == num:
            return False
    # check the box
    for i in range((row//3)*3, (row//3)*3 + 3):
        for j in range((col//3)*3, (col//3)*3 + 3):
            if board[i][j] == num:
                return False

    return True

# function to solve a sudoku puzzle for the given board recursively
def solve_sudoku(board):
    empty_cell = next_empty_cell(board)
    
    if empty_cell:
        row, col = empty_cell
    else:
        # if empty_cell is null, it means that the board is full, thus puzzle is solved
        return True

    for num in range(1, 10):
        if check_valid(board, num, row, col):
            # if number is valid at the position, try that number and continue
            board[row][col] = num

            # solve the rest of the board
            if solve_sudoku(board):
                return True
            
            # the board is unsolvable, so remove the number
            board[row][col] = 0

    return False




print_board(board)

print("SOLVING THE BOARD...")
solve_sudoku(board)

print_board(board)