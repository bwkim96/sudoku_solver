# Version 2 of Sudoku Solver: lets user setup the board

preset_board = [
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


# function to setup user's own board
def setup_board():

    user_board = [
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    ]

    print("\nEnter a number you would like in the cell marked 'X'.\nEnter a number from 1 - 9, or 0 to leave it empty.\nIf you want to go back to last cell, enter b.")
    i, j = 0, 0
    while i < 9:
        j = 0
        while j < 9:
            print()
            user_board[i][j] = 'X'
            print_board(user_board)
            cell = input("Enter number you want in X cell: ")
            if cell == 'b':
                if j == 0:
                    print("You are already at the first cell.")
                else:
                    user_board[i][j] = '_'
                    j -= 2
            elif not cell.isdigit():
                print("Not a number. Please enter a number between 1 and 9, or 0.")
                j -= 1
            elif 0 <= int(cell) <= 9:
                user_board[i][j] = int(cell)
            else:
                print("Invalid number. Please enter a number between 1 and 9, or 0.")
                j -= 1
            j += 1
        i += 1

    return user_board

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
            
            # the board is unsolvable with the current number at current position, so remove the number
            board[row][col] = 0

    return False



print("Would you like the solutions of:\n1. A preset board?\n2. A board of your own?")
setup = ""
while setup != "1" and setup != "2":
    setup = input("Pleaes enter 1 or 2: ")
    if setup != "1" and setup != "2":
        print("Please enter a valid choice.")

if setup == "1":
    print("\nSolving a preset board: ")
    board = preset_board
else:
    print("\nSetting up your own board...")

    board = setup_board()


print_board(board)

print("\nSOLVING THE BOARD...\n")

if solve_sudoku(board):
    print("Solve complete.")
    print_board(board)
else:
    print("Given sudoku puzzle is unsolvable.")