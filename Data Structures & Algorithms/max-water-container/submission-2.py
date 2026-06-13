class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        count = 0

        while left < right:
            if heights[left] < heights[right]:
                count = max(count, heights[left] * (right-left))
                left += 1
            elif heights[left] >= heights[right]:
                count = max(count, heights[right] * (right-left))
                right -= 1

            
        return count
