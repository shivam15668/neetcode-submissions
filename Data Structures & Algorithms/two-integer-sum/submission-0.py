class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i
        for i, num in enumerate(nums):
            j = target - num
            if j in seen and seen[j] != i:
                return [i, seen[j]]
        return []