import pygame

pygame.init()

sudoku = [
    [0,8,5, 0,0,2, 0,9,0],  # Line 1
    [0,0,0, 0,0,0, 0,2,6],
    [0,0,0, 7,0,0, 0,0,0],
    [0,0,0, 4,2,7, 0,0,0],  # Line 4
    [3,0,0, 0,1,5, 0,0,0],
    [0,9,0, 0,0,0, 0,0,5],
    [9,2,6, 8,0,0, 3,0,0],  # Line 7
    [0,0,0, 0,4,0, 7,0,0],
    [4,0,3, 0,0,0, 0,0,9]
]


# returns a bool is the Board is a valid board. calls valid_digit().
def valid_givens(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            num = board[i][j]
            if num != 0:
                if not valid_digit(board, num, (i, j)):
                    return False
    return True


# checks if the digit is a potentially valid solution
def valid_digit(board, digit, cell):

    # check the digit against the rest of the column
    for i in range(len(board)):
        if board[i][cell[1]] == digit and i != cell[0]:
            return False
    # check the digit against the rest of the row
    for j in range(len(board[0])):
        if board[cell[0]][j] == digit and j != cell[1]:
            return False
    # TIL: integer division // is the same as floordiv()
    col_offset = (cell[0] // 3) * 3
    row_offset = (cell[1] // 3) * 3
    # check the digit against the rest of the box
    for a in range(0, 3):
        for z in range(0, 3):
            if board[a + col_offset][z + row_offset] == digit:
                if a + col_offset != cell[0] and z + row_offset != cell[1]:
                    return False
    return True


def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(str(board[i][j]) + " ")
            else:
                print(str(board[i][j]) + " ", end="")


def next_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return (10, 10)


def sudoku_solve(board):
    empty_cell = next_blank(board)
    if empty_cell[0] < 10:
        for dig in range(1, 10):
            if valid_digit(board, dig, (empty_cell[0], empty_cell[1])):
                board[empty_cell[0]][empty_cell[1]] = dig
                return sudoku_solve(board)
                board[empty_cell[0]][empty_cell[1]] = 0
    else:
        return board

# def sudoku_solve(board):
#     empty_cell = next_blank(board)
#     if empty_cell[0] < 10:
#         for dig in range(1, 10):
#             if valid_digit(board, dig, (empty_cell[0], empty_cell[1])):
#                 board[empty_cell[0]][empty_cell[1]] = dig
#                 if sudoku_solve(board):
#                     return True
#                 board[empty_cell[0]][empty_cell[1]] = 0
#         return False
#     else:
#         return True



display_board(sudoku)
if valid_givens(sudoku):
    print("This Board State is Valid")
print(next_blank(sudoku))
print(sudoku_solve(sudoku))
display_board(sudoku)
if valid_givens(sudoku):
    print("This Solution is Valid")
