class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<1 or len(nums)>10**4 or target<-10**4 or target >10**4:
           return False    
        notfind=0
        for i in range(len(nums)):
           if nums[i]<-10**4 or nums[i]>10**4:
              return False
           if nums[i]==target:
              return i
              notfind=1
        if notfind==0:
          nums.append(target) 
          nums.sort()
          for i in range(len(nums)):
              if nums[i]==target:
                 return i
            
        
        