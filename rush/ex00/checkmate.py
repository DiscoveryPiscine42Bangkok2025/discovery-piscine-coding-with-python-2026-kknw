def checkmate(board: str):
    grid = []
    for row in board.splitlines():
        grid.append(list(row))
    #print(grid)

    if not grid:
        return

    # check if square
    boardSize = len(grid)
    for row in grid:
        if len(row) != boardSize:
            return
        
    # find King (K) position
    king_pos = None
    nKing = 0
    for row in range(boardSize):
        for col in range(boardSize):
            if grid[row][col] == 'K':
                king_pos = (row, col)
                nKing += 1
                if nKing > 1:
                    return
                #print("nKing = ",nKing)
                #print(king_pos)

    # no King (K)
    if nKing == 0:
        return
    
    k_row, k_col = king_pos

    def in_bounds(r, c):
        return 0 <= r < boardSize and 0 <= c < boardSize
    
    # Pawn (diag 1 forward)
    for dc in (-1, 1): #(left, right)
        r, c = k_row - 1, k_col + dc
        if in_bounds(r, c) and grid[r][c] == 'P':
            print("Success")
            return

    # Rook + Queen (straight line - long term)
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # up down left right
    for dr, dc in directions:
        r, c = k_row + dr, k_col + dc
        while in_bounds(r, c):
            piece = grid[r][c]
            if piece != '.':
                if piece in ('R','Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # Bishop + Queen (diag - long term)
    directions = [(-1,-1), (-1,1), (1,-1), (1,1)] # upL upR downL downR
    for dr, dc in directions:
        r, c = k_row + dr, k_col + dc
        while in_bounds(r, c):
            piece = grid[r][c]
            if piece != '.':
                if piece in ('B','Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")