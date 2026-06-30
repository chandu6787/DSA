class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r=len(mat)
        c=len(mat[0])
        index=-1
        max_count=-1
        for i in range(r):
            current_count=0
            for j in range(c):
                current_count+=mat[i][j]
            if current_count>max_count:
                max_count=current_count
                index=i
        return [index,max_count]

        