class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1 and len(s)>15:
            return False

        # Roman numeral mapping
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):
            # Check if this is a subtraction case
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2  # Skip both characters
            else:
                total += roman_map[s[i]]
                i += 1

        return total
