class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in  nums:
            count[num] = count.get(num,0)+1  # {1:3, 2:2}

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))

            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq,num in heap]