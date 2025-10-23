class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0 or n>45:
            return 0
       
        if n == 0 or n == 1:
            return 1

        prev, curr = 1, 1 
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr