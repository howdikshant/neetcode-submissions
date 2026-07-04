class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        m = len(matrix)
        n = len(matrix[0])


        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                left = 0
                right = n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        right = mid - 1
                    if matrix[i][mid] < target:
                        left = mid + 1

        return False
