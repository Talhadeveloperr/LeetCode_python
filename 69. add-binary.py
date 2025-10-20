class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<1 or len(a)>10**4 or len(b)<1 or len(b)>10**4:
           return False
        dec1 = int(a, 2)
        dec2 = int(b, 2)
        dec_sum = dec1 + dec2
        binary_sum = bin(dec_sum)[2:]
        return binary_sum