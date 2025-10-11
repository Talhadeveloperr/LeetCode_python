class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1 or len(nums) > 10**4:
            return False
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > 10**5:
                return False        
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return True
