class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<1 or len(nums)>6:
         return False
        for i in range(len(nums)):
          if nums[i]<-10 or nums[i]>10:
             return False
        def backtrack(start):
          if start == len(nums):
             result.append(nums[:])
             return
        
          for i in range(start, len(nums)):           
             nums[start], nums[i] = nums[i], nums[start]
             backtrack(start + 1)
             nums[start], nums[i] = nums[i], nums[start]
    
        result = []
        backtrack(0)
        return result