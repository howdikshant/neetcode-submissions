class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmp = {}

        for num in nums:
            if num not in hmp:
                hmp[num] = 0
            hmp[num] += 1
        sort_mp = [e for e, v in sorted(hmp.items(), key=lambda x:x[1], reverse=True)]

        return (sort_mp[:k])

        


        