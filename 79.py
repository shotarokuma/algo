class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(board, curr, dp, word, i):
            if i == len(word):
                return True
            v = curr[0]
            h = curr[1]
            if  v < 0 or h < 0 or len(board) <= v or len(board[0]) <= h:
                return False
            if board[v][h] != word[i] or not dp[v][h]:
                return False
            dp[v][h] = False
            return helper(board, [v - 1,h], dp, word, i + 1) or helper(board, [v,h - 1], dp, word, i + 1) or helper(board, [v + 1,h], dp, word, i + 1)  or helper(board, [v,h + 1], dp, word, i + 1) 
        
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                curr = [i, j]
                k = 0
                dp = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
                if helper(board, curr, dp, word, k):
                    return True
        return False
                        
                        
                        
                        
                    
                    
                