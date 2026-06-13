class Solution:
    def required_time(self,piles,speed):
        total_hours=0
        for pile in piles:
            total_hours+=ceil(pile/speed)
        return total_hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            if self.required_time(piles,mid)>h:
                low=mid+1
            elif self.required_time(piles,mid)<=h:
                high=mid-1
        return low
        

        