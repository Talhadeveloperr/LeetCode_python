class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x<-100.0 or x>100.0 or n<-2**31 or n>2**31-1:
           return False
        f=float(x**n)
        if f<-10**4 or f>10**4:
           return False
        return f