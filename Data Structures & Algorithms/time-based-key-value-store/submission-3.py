class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeMap:
            return ""

        arr = self.timeMap[key]
        ans = ""
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]

                l = mid + 1
            else:
                r = mid - 1

        return ans
