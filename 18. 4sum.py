class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()

        if len(nums) < 1 or len(nums) > 200:
            return res
        if target < -10**9 or target >10**9:
            return res

        for i in range(len(nums) - 3):
            if nums[i] > 10**9 or nums[i] < -10**9:
                return []
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, len(nums)-1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

