class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for j in range(cols)] for _ in range(rows)]
        if(obstacleGrid[0][0] == 1):
            return 0
        dp[0][0] = 1
        for j in range(1,cols):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                for m in range(j+1,cols):
                    dp[0][m] = 0
                break
            else:
                dp[0][j] = 1
                
                
        for i in range(1,rows):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                for m in range(i+1,rows):
                    dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
        
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        
        return dp[rows-1][cols-1]
        
        
                    
                    
        
