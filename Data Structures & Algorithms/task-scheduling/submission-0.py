from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        heap = []
        for i in freq.values():
            heapq.heappush(heap,-i)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if queue and queue[0][1] == time:
                val, _ = queue.popleft()
                heapq.heappush(heap, val)

            
            if heap:
                a = heapq.heappop(heap)
                a += 1
                if a != 0:
                    queue.append((a, time + n + 1))

        return time
            


        
