class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid.at(0).size();
        
        int dp[rows][cols];
        
        dp[0][0] = grid.at(0).at(0);
        
        for(int i=1;i<cols;i++)
        {
            dp[0][i] = dp[0][i-1] + grid.at(0).at(i);
        }
        
        for(int j=1;j<rows;j++)
        {
            dp[j][0] = dp[j-1][0] + grid.at(j).at(0);
        }
        
        for(int m=1;m<rows;m++)
        {
            for(int n=1;n<cols;n++)
            {
                int value = grid.at(m).at(n);
                dp[m][n] = min(dp[m-1][n]+value, dp[m][n-1]+value);
            }
        }
        
        return dp[rows-1][cols-1];    
        
    }
};
