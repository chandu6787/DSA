class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                ans.append(newInterval)
                return ans+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        ans.append(newInterval)
        return ans
