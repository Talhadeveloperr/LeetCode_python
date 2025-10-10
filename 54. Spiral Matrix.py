class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        n = len(matrix[0])
    
        # Validate matrix size
        if m < 1 or n > 10:
         return False
    
        # Validate matrix values
        for i in range(m):
         for j in range(n):
             if matrix[i][j] < -100 or matrix[i][j] > 100:
                 return False
    
        # Spiral traversal
        while matrix:
         # 1️⃣ Take first row
         res += matrix.pop(0)
        
         # 2️⃣ Take last column
         if matrix and matrix[0]:
             for row in matrix:
                 res.append(row.pop(-1))
        
         # 3️⃣ Take last row in reverse
         if matrix:
             res += matrix.pop(-1)[::-1]
        
         # 4️⃣ Take first column (bottom to top)
         if matrix and matrix[0]:
             for row in matrix[::-1]:
                 res.append(row.pop(0))
                
        return res