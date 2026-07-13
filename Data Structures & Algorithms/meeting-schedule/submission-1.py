"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals[1:]:
            s = interval.start
            e = interval.end
            if s < end:
                return False
            else:
                start = s
                end = e
        return True