class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        if len(nums) < 3 or len(nums) > 3000:
            return res

        for i in range(len(nums)):
            if nums[i]>10**5 or nums[i]<-10**5:
                return []
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicates
                continue

            x = nums[i]
            y = i + 1
            z = len(nums) - 1

            while y < z:
                total = x + nums[y] + nums[z]

                if total == 0:
                    res.append([x, nums[y], nums[z]])
                    # Skip duplicates
                    while y < z and nums[y] == nums[y+1]:
                        y += 1
                    while y < z and nums[z] == nums[z-1]:
                        z -= 1
                    y += 1
                    z -= 1
                elif total < 0:
                    y += 1
                else:
                    z -= 1

        return res
