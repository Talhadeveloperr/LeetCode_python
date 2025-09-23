class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<1 or len(nums)>3*10**4:
            return False
        i=0
        while i < len(nums)-1:
            if nums[i]<-100 or nums[i]>100:
                return False
            if nums[i]==nums[i+1]:
                nums.pop(i+1)    
            else:
                i+=1
        return len(nums)        
