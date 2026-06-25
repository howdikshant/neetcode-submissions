class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        nums.sort()

        def dfs(i, total):
            
            if total == target:
                res.append(sub.copy())
                return
            if total > target or i == len(nums):
                return 

            sub.append(nums[i])
            dfs(i+1, total + nums[i])


            sub.pop()


            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, total)

        dfs(0, 0)

        return res