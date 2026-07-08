class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            if y > x:
                x, y = y, x
            heapq.heappush(heap, -(x-y))

        if heap:
            return -heap[0]
        else:
            return 0



            

        


        