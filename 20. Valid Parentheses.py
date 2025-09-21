class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<1 or len(s)>10**4:
            return False
        stack = []
        
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  
              
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char) 

        return not stack
