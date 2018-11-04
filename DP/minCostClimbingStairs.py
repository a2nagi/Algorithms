class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = [0 for i in range(length)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,length):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        
        return min(dp[length-1], dp[length-2])
            
        
        
        
