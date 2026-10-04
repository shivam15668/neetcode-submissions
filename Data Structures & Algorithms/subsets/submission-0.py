class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):

            # base case

            if i == len(nums):
                result.append(subset.copy())
                return
            
            #choice 1 include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            
            #choice 2 undo choice 1 - dont include nums[i]
            subset.pop()

            backtrack(i+1)

        backtrack(0)

        return result
