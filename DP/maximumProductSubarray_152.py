class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 0:
            return 0
        
        prev_min = nums[0]
        prev_max = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]
        
        global_max = nums[0]
        
        for i in range(1,length):
            cur_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            cur_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])
            prev_max = cur_max
            prev_min = cur_min
            global_max = max(cur_max, global_max)
        return global_max
            
        
