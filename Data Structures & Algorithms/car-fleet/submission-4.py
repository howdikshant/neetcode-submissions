class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        if not cars:
            return 0
        cars.sort(reverse=True)
        time = []
        for p,s in cars:
            time.append((target - p) / s)
        curr = time[0]
        fleets = 1
        for i in time:
            if i <= curr:
                continue
            elif i > curr:
                fleets += 1
                curr = i
        
        return fleets

        
        