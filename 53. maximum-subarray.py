class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1 or len(nums)>10**5:
           return False
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
          if num<-10**4 or num>10**4:
             return False
          current_sum += num
          if current_sum > max_sum:
             max_sum = current_sum
          if current_sum < 0:
             current_sum = 0

        return max_sum
