class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        arr = [0] * len(nums)

        prod = 1
        for i in range(len(nums)):
            left[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = prod
            prod *= nums[i]

        for i in range(len(nums)):
            arr[i] = left[i] * right[i]
        return arr
        


        

        
            
        