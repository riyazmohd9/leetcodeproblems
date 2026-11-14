class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_count,ten_count = 0,0
        for i in bills:
            if i == 5:
                five_count += 1
            elif i == 10:
                if five_count >0:
                    five_count -= 1
                    ten_count += 1
                else:
                    return False
            elif i == 20:
                if five_count>0 and ten_count >0:
                    five_count -= 1
                    ten_count -= 1
                elif five_count>=3:
                    five_count -= 3
                else:
                    return False
        return True


       

        