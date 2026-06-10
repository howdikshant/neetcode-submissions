class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        

        left = 1
        right = m
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
                
            if hours <= h:
                right = mid - 1
                ans = mid

            else: 
                left = mid + 1
            
        return ans 

        