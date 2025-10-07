class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)<1 or len(strs)>10**4:
         return False
        anagrams = {}
        i=0
        for word in strs:
         if len(strs[i])<0 or len(strs[i])>100:
             return False
         i+=1
         key = ''.join(sorted(word))
         if key not in anagrams:
             anagrams[key] = []
         anagrams[key].append(word)
        return list(anagrams.values())