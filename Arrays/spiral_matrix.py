class Solution(object):
    def append_layer(self, matrix, layer, vector, last):
        i = layer
        j = layer
        rows = len(matrix)
        cols = len(matrix[0])
        while i < cols - layer:
            vector.append(matrix[layer][i])
            i += 1
        
        i = layer+1
        while i < rows-layer:
            vector.append(matrix[i][cols-layer-1])
            i += 1
        if last == False:
            i = cols-layer-2
            while i>=layer:
                print (layer)
                vector.append(matrix[rows-layer-1][i])
                i -= 1

            i = rows-layer-2
            while i > layer:
                print ("Here 1", layer)
                vector.append(matrix[i][layer])
                i -= 1
            
            
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        vector = []
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        layer = 0
        while(i < rows and j <cols):
            if (layer+1)*2 > rows or (layer+1)*2 > cols:
                self.append_layer(matrix, layer, vector, True)
            else:
                self.append_layer(matrix, layer, vector, False)
            i += 2
            j += 2
            layer += 1
        
        return vector
            
