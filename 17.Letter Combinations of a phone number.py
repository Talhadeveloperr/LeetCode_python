class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        
        if len(digits) < 0 or len(digits) > 4:
            return []   
        for d in digits:
            if d < "2" or d > "9":
                return []  

        if not digits:   
            return []

        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = [""]

        for digit in digits:
            new_result = []
            for prefix in result:
                for letter in letters[digit]:
                    new_result.append(prefix + letter)
            result = new_result

        return result
