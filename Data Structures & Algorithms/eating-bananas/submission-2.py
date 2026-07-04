class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = max(piles)
        while left <= right:
            s = 0
            mid = left + (right - left) // 2
            
            for pile in piles:
                s += math.ceil(pile / mid)
            if s > h:
                left = mid + 1
            if s <= h:
                ans = mid
                right = mid -1
                
                
        return ans

        