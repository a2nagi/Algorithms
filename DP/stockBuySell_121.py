class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        array=[]
        array.append(0)
        length = len(prices)
        curmin = prices[0]
        for i in range(1,length):
            if curmin > prices[i]:
                curmin = prices[i]
            array.append(prices[i]-curmin)
        return max(array)
