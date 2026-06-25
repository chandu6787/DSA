class Solution:
    def possible(self,bloomDay,m,k,day):
        noOfBouques=0
        cntDays=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                cntDays+=1
            else:
                noOfBouques+=(cntDays)//k
                cntDays=0
        noOfBouques+=(cntDays)//k
        if noOfBouques>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low,high=min(bloomDay),max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while low<=high:
            mid=(low+high)//2
            if self.possible(bloomDay,m,k,mid):
                high=mid-1
            else:
                low=mid+1
        return low

        return -1      