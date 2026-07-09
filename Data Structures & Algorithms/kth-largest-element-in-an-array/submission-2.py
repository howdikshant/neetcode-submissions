class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        if not nums:
            return 0
        if k > len(nums):
            return 0
        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)