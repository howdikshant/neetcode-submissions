class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        for i in range(len(temp)):
            
           
            while stack and temp[stack[-1]] < temp[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res
        

         

        

        

        