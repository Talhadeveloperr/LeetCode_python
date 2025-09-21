class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<1 or n>8:
            return False
        result = []

        def backtrack(current, open_count, close_count):
            # If the string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if possible
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result