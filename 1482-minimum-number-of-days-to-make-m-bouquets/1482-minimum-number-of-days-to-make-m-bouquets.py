class Solution:
    def possibility(self,bloomDay,assumeDay,m,k):
        cnt=0
        noofBouq=0
        for day in bloomDay:
            if day<=assumeDay:
                cnt+=1
            else:
                noofBouq+=(cnt)//k
                cnt=0
        noofBouq+=(cnt)//k
        if noofBouq>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low,high=min(bloomDay),max(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.possibility(bloomDay,mid,m,k)==True:
                high=mid-1
            else:
                low=mid+1
        if low<=max(bloomDay):
            return low
        else:
            return -1

        