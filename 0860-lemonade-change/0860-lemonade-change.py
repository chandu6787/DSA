class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives,tens=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                fives+=1
            elif bills[i]==10:
                if fives>0:
                    tens+=1
                    fives-=1
                else:
                    return False
            else:
                if fives and tens:
                    fives-=1
                    tens-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True


        