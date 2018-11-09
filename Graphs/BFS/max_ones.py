class Solution(object):
    def count_ones(self, nums, i):
        index_left = i-1
        index_right = i+1
        count = 0
        while index_left >= 0 and nums[index_left] == 1:
            count += 1
            index_left -= 1
            
        while index_right < len(nums) and nums[index_right] == 1:
            count += 1
            index_right += 1
        
        return count+1
        
        
        
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        global_max = 0
        seen_0 = False
        for i in range(length):
            if nums[i] == 0:
                seen_0 = True
                count = self.count_ones(nums, i)
                global_max = max(count, global_max)
        if seen_0 == False:
            return length
        return global_max
        
