class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        end_time=float('-inf')
        res=0
        intervals.sort(key=lambda x:x[1])
        for start,end in intervals:
            if start>=end_time:
                end_time=end
            else:
                res+=1
        return res
