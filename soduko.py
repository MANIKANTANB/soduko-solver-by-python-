def sudoku_solver(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1,10):
        if is_valid(board, (row, col), num):
            board[row][col] = num

            if sudoku_solver(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, pos, num):
    # Check row
    for col in range(9):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check col
    for row in range(9):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y*3, box_y*3 + 3):
        for col in range(box_x * 3, box_x*3 + 3):
            if board[row][col] == num and (row,col) != pos:
                return False

    return True

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
sudoku_solver(board)

for row in board:
    print(row)
