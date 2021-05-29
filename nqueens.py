def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        def solve(board, row):
            for j in range(len(board)):
                new_board = create_board(board, row, j)
                if check(new_board):
                    if row == n - 1: add_board(new_board)
                    else: solve(new_board, row + 1)
        
        def create_board(board, row, col):
            new_board = []
            for i in range(len(board)):
                if i != row:
                    new_board.append(board[i])
                else:
                    new_row = []
                    for j in range(len(board)):
                        if j != col:
                            new_row.append('.')
                        else:
                            new_row.append('Q')
                    new_board.append(new_row)
            return new_board
        
        def add_board(board):
            new_board = []
            for row in board:
                new_board.append(''.join(row))
            solutions.append(new_board)
        
        def check(board):
            # Check Rows
            # for i in range(len(board)):
            #     if board[i].count('Q') > 1:
            #         return False

            # Check Columns
            for j in range(len(board)):
                count = 0
                for i in range(len(board)):
                    if board[i][j] == 'Q':
                        count += 1
                    if count > 1: return False
            
            # Check Diagnols
            starts1 = [(0, i) for i in range(len(board))]
            starts1.extend([(j, 0) for j in range(1, len(board))])
            for start in starts1:
                i, j = start
                count = 0
                while i < len(board) and j < len(board):
                    if board[i][j] == 'Q':
                        count += 1
                    i += 1
                    j += 1
                if count > 1: return False
                
            starts2 = [(0, i) for i in range(len(board))]
            starts2.extend([(j, len(board) - 1) for j in range(1, len(board))])
            for start in starts2:
                i, j = start
                count = 0
                while i < len(board) and j >= 0:
                    if board[i][j] == 'Q':
                        count += 1
                    i += 1
                    j -= 1
                if count > 1: return False
            return True
        
        
        board = ['.' * n] * n
        solve(board, 0)
        
        return solutions
