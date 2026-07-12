class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            last = ans[-1]
            if s > last[1]:
                ans.append([s, e])

            else:
                last[1] = max(last[1], e)

        return ans

            
