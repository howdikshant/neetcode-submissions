class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmp = {}

        for num in nums:
            if num in hmp:
                hmp[num] += 1
            else:
                hmp[num] = 1

        sorted_items = sorted(hmp.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

            
