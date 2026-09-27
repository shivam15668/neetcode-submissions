class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 != stone2:
                difference  = (stone1 - stone2)
                heapq.heappush(stones, -difference)


        return -stones[0] if stones else 0