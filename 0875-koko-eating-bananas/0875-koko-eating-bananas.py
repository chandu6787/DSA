class Solution:
    def total_hours(self,speed,piles):
        hours_sum=0
        for pile in piles:
            hours_sum+=ceil(pile/speed)
        return hours_sum

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            if self.total_hours(mid,piles)<=h:
                high=mid-1
            else:
                low=mid+1

        return low
        
        