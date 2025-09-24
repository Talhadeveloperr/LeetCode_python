class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) <0 or len(nums) > 100 or val < 0 or val > 100:
            return False
        i=0
        while i < len(nums):
          if nums[i] < 0 or nums[i] > 50:
              return False
          if nums[i]==val:
              nums.pop(i)
          else:
              i+=1 
        return len(nums)         
   

        