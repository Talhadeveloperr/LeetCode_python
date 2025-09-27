class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<0 or len(nums)>10**5 or target<-10**9 or target>10**9:
         return False
        find=[]
        res=[]
        for i in range(len(nums)):
         if nums[i]<-10**9 or nums[i]>10**9:
             return False
         if nums[i]==target:
             find.append(i)
        if len(find)==0:
           return [-1,-1]
        if len(find)>0:            
          res.append(find[0])
          res.append(find[-1])           
          return res        
        