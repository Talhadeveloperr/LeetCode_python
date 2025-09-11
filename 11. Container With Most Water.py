class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Constraints:
        n == len(height)
        2 <= n <= 10^5
        0 <= height[i] <= 10^4
        """
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            # calculate current area
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            # move the pointer with smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
