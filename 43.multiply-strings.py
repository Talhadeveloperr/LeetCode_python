class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1)<1 or len(num1)>200 or len(num2)<1 or len(num2)>200:
          return False
        n1=int(num1)
        n2=int(num2)
        m=n1*n2
        r=str(m)
        return r