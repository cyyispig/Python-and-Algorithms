class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(x, y, index):
            if index == len(word):
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[index]:
                    board[nx][ny] = '/'
                    if dfs(nx, ny, index + 1):
                        return True
                    board[nx][ny] = word[index]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '/'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False
