class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        if n<1 or n>20:
            return False
        for i in range(n):
            if len(matrix[i])!=n:
                return False
            for j in range(i + 1, n):
                if matrix[i][j]<-1000 or matrix[i][j]>1000:
                    return False
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]      
        for row in matrix:
            row.reverse()
