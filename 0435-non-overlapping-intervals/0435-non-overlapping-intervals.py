class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        cnt=0
        end_time=float('-inf')
        for s,e in intervals:
            if s>=end_time:
                end_time=e
                cnt+=1
        return n-cnt
        