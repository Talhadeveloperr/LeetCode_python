class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        if len(nums)<3 or len(nums)>500 or target<-10**4 or target>10**4:
            return False
        for i in range(len(nums)):
            if nums[i]>1000 or nums[i]<-1000:
                return False

        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # If exact match, return immediately
                if total == target:
                    return total

                # Update closest_sum if closer
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                # Move pointers
                if total < target:
                    l += 1
                else:
                    r -= 1

        return closest_sum