class MedianFinder:

    def __init__(self):
        self.left = []  #max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]:
            left_max = -heapq.heappop(self.left)
            right_min = heapq.heappop(self.right)

            heapq.heappush(self.left, -right_min)
            heapq.heappush(self.right, left_max)

        if len(self.left) > len(self.right) + 1 :
            heapq.heappush(self.right, - heapq.heappop(self.left))
        
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) - len(self.right) == 1:
           return -self.left[0]
        else:
            return (-self.left[0] + self.right[0])/2
        