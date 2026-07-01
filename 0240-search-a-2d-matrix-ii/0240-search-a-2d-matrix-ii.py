from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            index=bisect_left(matrix[i],target)
            if index<n and matrix[i][index]==target:
                return True
            
        return False

        