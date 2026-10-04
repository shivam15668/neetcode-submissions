class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = set()

        def backtracking():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)

                backtracking()
                path.pop()

                used.remove(num)
        backtracking()

        return result