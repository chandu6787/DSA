class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n=len(bills)
        five,ten=0,0
        for note in bills:
            if note==5:
                five+=1
            elif note==10:
                if five:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if ten and five:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True