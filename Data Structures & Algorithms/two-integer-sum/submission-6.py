class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in hmp:
                return [hmp[comp], i]
            hmp[num] = i
        