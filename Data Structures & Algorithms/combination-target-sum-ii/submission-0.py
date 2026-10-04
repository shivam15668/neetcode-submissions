class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            
            elif remaining <0:
                return 
            
            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i]> target:
                    break
                path.append(candidates[i])
                backtrack(i+1,path, remaining - candidates[i])
                path.pop()

        backtrack(0,path, target)

        return result