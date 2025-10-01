class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1 or n > 30:
            return False
        if n == 1:
            return "1"
        else:
            s = "1"
            for j in range(2, n + 1):  
                result = ""
                i = 0
                while i < len(s):
                    count = 1
                    while i + 1 < len(s) and s[i] == s[i + 1]:
                        count += 1
                        i += 1
                    result += str(count) + s[i]
                    i += 1
                s = result  
            return s  