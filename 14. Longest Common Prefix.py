class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  
            return ""       
        if len(strs)<1 or len(strs)>200:
            return 0
        for i in range(len(strs)):
           if len(strs[i])<0 or len(strs[i])>200:
              return False   
        prefix = strs[0]    
        
        for s in strs[1:]:           
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""        
        return prefix
