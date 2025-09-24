class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) <1 or len(needle) > 10**4 or len(haystack) < 1 or len(haystack)> 10**4:
            return False
        if len(needle) and len(haystack):
            return(haystack.find(needle))
        else:
            return -1     