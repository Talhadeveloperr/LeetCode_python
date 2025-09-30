def isValidSudoku(board):
    seen = set()
    if len(board)!=9:
        return False
    for i in range(len(board)):       
        if len(board[i])!=9:
            return False

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue

            # Create unique keys for row, column, and box
            row_key = (num, "row", r)
            col_key = (num, "col", c)
            box_key = (num, "box", r // 3, c // 3)

            # If already seen in any row/col/box, it's invalid
            if row_key in seen or col_key in seen or box_key in seen:
                return False

            seen.update([row_key, col_key, box_key])

    return True