class Solution:
    def helper(self,weights,capacity):
        days,load=1,0
        for i in range(0,len(weights)):
            if load+weights[i]>capacity:
                days+=1
                load=weights[i]
            else:
                load+=weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if self.helper(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
        return low

        return -1

        