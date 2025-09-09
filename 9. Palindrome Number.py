class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative numbers are never palindromes
        if x < 0:
            return False
        
        # convert number to list of digits
        arr = [int(digit) for digit in str(x)]
        
        # reverse list
        rev = arr[::-1]
        
        # check palindrome and integer bounds
        if arr == rev and -2**31 < x < 2**31 - 1:
            return True
        else:
            return False
