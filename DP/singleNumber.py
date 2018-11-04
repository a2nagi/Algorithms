class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_store = {}
        for x in nums:
            if x in dict_store:
                dict_store[x] += 1
            else:
                dict_store[x] = 1
        
        answer = []
        for key in dict_store:
            if dict_store[key] == 1:
                answer.append(key)
        return answer
                
            
        
