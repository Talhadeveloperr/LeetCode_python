class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest=""


        for i in range(n):
             for j in range(i+1, n+1):
                 sub = s[i:j]               
                 if sub == sub[::-1] and len(sub) > len(longest):  
                     longest=sub
        return longest             
        