class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1 or len(nums)>10**4:
          return False
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0
    
        for i in range(n - 1):
           if nums[i]<0 or nums[i]>1000:
             return False       
           farthest = max(farthest, i + nums[i])
           if i == current_end:
              jumps += 1
              current_end = farthest
        return jumps