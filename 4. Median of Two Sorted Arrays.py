class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=nums1 +nums2
        n.sort()
        l=len(n)
        if l % 2 == 0:
            median=(n[l//2-1]+ n[l//2]) / 2.0
        else:
            median =n[l//2]
        return median     
               

        