from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                matrix_left, matrix_right = 0, len(matrix[middle]) - 1
                while matrix_left <= matrix_right:
                    matrix_middle = matrix_left + (matrix_right - matrix_left) // 2
                    if target == matrix[middle][matrix_middle]:
                        return True
                    elif target < matrix[middle][matrix_middle]:
                        matrix_right = matrix_middle - 1
                    else:
                        matrix_left = matrix_middle + 1
                return False
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                left = middle + 1
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0))


