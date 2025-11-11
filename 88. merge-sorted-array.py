class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m<0 or m>200 or n<0 or n>200 or (m+n)<0 or (m+n)>200:
            return False
        i=0

        for i in range(n):
            nums1.pop(-1)
        nums1.extend(nums2)
        nums1.sort()
        for i in range(len(nums1)):
            if nums1[i]<-10**9 or nums1[i]>10**9:
                return False
        return len(nums1)

            

