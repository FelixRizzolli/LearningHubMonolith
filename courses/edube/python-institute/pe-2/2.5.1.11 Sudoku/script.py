def read_sudoku_board() -> list[list[str]]:
    sudoku_board: list[list[str]] = []
    for i in range(9):
        row = input(f"Input row {i + 1}: ")
        if len(row) != 9 or not row.isdigit():
            raise ValueError("Input not valid")
        sudoku_board.append(list(row))
    return sudoku_board


def is_valid_group(group: list[str]) -> bool:
    # Checks if group contains all digits 1-9 exactly once
    return sorted(group) == [str(d) for d in range(1, 10)]


def validate_board(board: list[list[str]]) -> bool:
    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False
    # Check 3x3 sub-squares
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            sub_square = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(sub_square):
                return False
    return True


sudoku_board = read_sudoku_board()
print("Yes" if validate_board(sudoku_board) else "No")
