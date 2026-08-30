class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for num in nums:   # [1,1,1,2,2,3]
            count[num] = count.get(num,0)+1 #{1:3, 2:2, 3:1}
        
        buckets = [[] for _ in range(len(nums)+ 1)]
        for num,freq in count.items():
            buckets[freq].append(num)    # 0[] , 1[3]  , 2[2]

        result = []

        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
            if len(result) == k:
                return result