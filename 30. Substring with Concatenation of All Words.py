class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # ---------------- Constraints ----------------
        if len(s) < 1 or len(s) > 10**4:
            return []
        if len(words) < 1 or len(words) > 5000:
            return []
        for w in words:
            if len(w) < 1 or len(w) > 30:
                return []
        # ---------------------------------------------

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []

        # Build frequency map of words
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        res = []

        # Sliding window over s
        for i in range(word_len):  
            left = i
            count = 0
            seen = {}
            for j in range(i, len(s) - word_len + 1, word_len):
                w = s[j:j+word_len]
                if w in word_count:
                    seen[w] = seen.get(w, 0) + 1
                    count += 1

                    # If a word appears too many times, shrink window
                    while seen[w] > word_count[w]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Found a valid window
                    if count == num_words:
                        res.append(left)

                else:  # reset if invalid word
                    seen.clear()
                    count = 0
                    left = j + word_len

        return res
