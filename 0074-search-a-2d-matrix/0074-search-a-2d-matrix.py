from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            current_index=bisect_left(matrix[i],target)
            if current_index<c and matrix[i][current_index]==target:
                return True
        return False
        