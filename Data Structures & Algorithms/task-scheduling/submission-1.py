class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       count = Counter(tasks)
       heap  = [-freq for freq in count.values()]
       heapq.heapify(heap)

       # frequency, time_when_available
       queue = deque()
       time = 0 
       while heap or queue:
        time += 1
        if heap:
            freq = heapq.heappop(heap)

            freq += 1

            if freq != 0 :
                queue.append((freq, time+n))
            
        if queue and queue[0][1] == time:
                freq,_ = queue.popleft()
                heapq.heappush(heap, freq)

       return time

