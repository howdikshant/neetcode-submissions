class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        curr = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                count = max(count, curr)
                curr = 1
        count = max(count, curr)
        return count
            
        