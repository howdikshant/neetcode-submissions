class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            comp = 0
            for j in range(i + 1, len(numbers)):
                comp = target - numbers[i]
                if numbers[j] == comp:
                    return [i+1, j+1]
