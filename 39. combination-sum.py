class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(candidates)<1 or len(candidates)>30 or target <1 or target >40:
           return False
        for i in range(len(candidates)):
           if candidates[i]<2 or candidates[i]>40:
              return False
        def backtrack(start, target, path):
          if target == 0:
             result.append(path[:])  
             return
          if target < 0:
             return
    
          for i in range(start, len(candidates)):
              path.append(candidates[i])
              backtrack(i, target - candidates[i], path)
              path.pop()

        backtrack(0, target, [])
        return result
