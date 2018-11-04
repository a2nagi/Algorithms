class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        size = len(nums)
        max_length = 1
        j = 0
        for i in range(1,size):
            if nums[i] <= nums[i-1]:
                j = i
            else:
                max_length = max(max_length, i-j+1)
        return max_length
       
