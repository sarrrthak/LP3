# N-Queens Problem using Backtracking

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):

    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueen(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


# Input
n = int(input("Enter number of queens: "))

board = [[0 for j in range(n)] for i in range(n)]

# Place first queen in the first row
first_col = int(input("Enter column for first queen (1 to n): ")) - 1

if n < 1 or first_col < 0 or first_col >= n:
    print("Invalid input")

else:
    board[0][first_col] = 1

    if solve_nqueen(board, 1, n):
        print("\nN-Queens Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists for this first queen position.")