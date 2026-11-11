class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res=[]
        for start,end in intervals:
            if not res or res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1]=max(res[-1][1],end)
        return res
        