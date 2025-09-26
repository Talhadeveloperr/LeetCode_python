class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<1 or len(nums)>5000 or target <-10**4 or target >10**4:
            return False
        find=False
        for i in range(len(nums)):
            if nums[i]<-10**4 or nums[i]>10**4:
                return False
            if nums[i]==target:
                return i
                find=True 
        if find==False:
          return -1                
    