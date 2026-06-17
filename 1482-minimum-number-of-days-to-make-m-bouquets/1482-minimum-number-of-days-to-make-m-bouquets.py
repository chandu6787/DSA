class Solution:
    def possible(self,bloomDay,day,m,k):
        count_flowers=0
        bouques=0
        for item in bloomDay:
            if item<=day:
                count_flowers+=1
            else:
                bouques+=(count_flowers//k)
                count_flowers=0
        bouques+=(count_flowers//k)
        if bouques>=m:
            return True
        else:
            return False


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low,high=min(bloomDay),max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while low<=high:
            mid=(low+high)//2
            if self.possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1

        return low
        