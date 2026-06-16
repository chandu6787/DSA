class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current=1
        missing_count=0
        while True:
            if current not in arr:
                missing_count+=1
                if missing_count==k:
                    return current
            current+=1
        return -1
                
        