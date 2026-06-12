class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if -nums[i] > nums[left] + nums[right]:
                    left += 1
                elif -nums[i] < nums[left] + nums[right]:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]

                    if triplet not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                

        return res