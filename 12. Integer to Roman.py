class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >3999 or num<1:
            return False

        # Mapping of values to symbols (including subtractive forms)
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        result = []
        
        # Greedy approach
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result.append(symbols[i])
        
        return "".join(result)
