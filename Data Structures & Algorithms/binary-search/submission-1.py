class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1;
        left = 0

        while left <= right:
            mid = (right + left) // 2

            

            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            if target == nums[mid]:
                return mid
        return -1