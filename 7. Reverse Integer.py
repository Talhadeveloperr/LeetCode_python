class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign =-1 if x<0 else 1

        y=str(abs(x))[::-1]
        
        x=sign * int(y)
        if x<-2**31 or x >2**31-1:
            return 0
        return x
        


        