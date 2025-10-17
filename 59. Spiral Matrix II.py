class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<1 or n>20:
            return False
        res = [[0 for _ in range(n)] for _ in range(n)]
        x = [i + 1 for i in range(n * n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        index = 0
        
        while index < n * n:
            # Fill top row (left → right)
            for i in range(left, right + 1):
                res[top][i] = x[index]
                index += 1
            top += 1
        
            # Fill right column (top → bottom)
            for i in range(top, bottom + 1):
                res[i][right] = x[index]
                index += 1
            right -= 1
        
            # Fill bottom row (right → left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = x[index]
                    index += 1
                bottom -= 1
        
            # Fill left column (bottom → top)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res[i][left] = x[index]
                    index += 1
                left += 1
        
        new=[]
        # Print matrix
        for row in res:
            new.append(list(row))
        return new 
