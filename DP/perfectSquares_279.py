def numSquares(n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
            
        dp = [[0 for i in range(n+1)] for _ in range(len(squares)+1)]
        
        for i in range(1, n+1):
            dp[0][i] = i
        
        for j in range(1, len(squares)+1):
            dp[j][0] = squares[j-1]
            
        for i in range(1, len(squares)+1):
            for j in range(1, n+1):
                if dp[i][0] == dp[0][j]:
                    dp[i][j] = 1
                    
                elif dp[i][0] > dp[0][j]:
                    dp[i][j] = dp[i-1][j]
                
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-dp[i][0]], 1+dp[i][j-1])

        
        return dp[len(squares)][n]
