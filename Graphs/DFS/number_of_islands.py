class Solution(object):
    def nuetralize(self, grid, i, j):
        if i<0 or i>= len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.nuetralize(grid, i+1,j)
        self.nuetralize(grid, i-1,j)
        self.nuetralize(grid, i,j+1)
        self.nuetralize(grid, i,j-1)
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    self.nuetralize(grid, i, j)
        return count
                    
