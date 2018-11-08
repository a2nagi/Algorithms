class Solution(object):
    def dfs_check(self, board, word, i, j, index):
        
        if index == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        
        
        current = board[i][j]
        board[i][j] = "*"
        result = self.dfs_check(board, word, i+1, j, index+1) or self.dfs_check(board, word, i-1, j, index+1) or self.dfs_check(board, word, i, j-1, index+1) or self.dfs_check(board, word, i, j+1, index+1)
           
        board[i][j] = current
        return result
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        first_char = word[0]
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == first_char:
                    if(self.dfs_check(board, word,i,j,0)):
                        return True
        return False
        
