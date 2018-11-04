class Solution(object):
       
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        rows = len(matrix)
        if len(matrix) == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][cols-1] >= target:
                start = 0
                end = len(matrix[i])-1
                while start <= end:
                    middle = (start + end)/2
                    if matrix[i][middle] == target:
                        return True
                    elif matrix[i][middle] > target:
                        end = middle-1
                    else:
                        start = middle+1       
        return False
    
            
        
