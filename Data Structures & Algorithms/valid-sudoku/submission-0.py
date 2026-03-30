class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows , cols , grid = [[] for i in range(len(board))] , [[] for i in range(len(board))] , [[] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grid[(i // 3) * 3 + (j // 3)]:
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                grid[(i // 3) * 3 + (j // 3)].append(board[i][j])
        return True
                