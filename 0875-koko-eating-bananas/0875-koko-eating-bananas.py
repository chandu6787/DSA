class Solution:
    def possible(self,piles,h,speed):
        totalHours=0
        for i in range(len(piles)):
            totalHours+=ceil(piles[i]/speed)
        if totalHours<=h:
            return True
        else:
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=0
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            if self.possible(piles,h,mid):
                high=mid-1
            else:
                low=mid+1
        return low


        