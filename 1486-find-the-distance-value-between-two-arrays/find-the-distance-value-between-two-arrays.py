class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        for i in arr1:
            arr3 = []
            for j in arr2:
                if abs(i-j)<= d:
                    arr3.append(1)
                else:
                    arr3.append(0)
            if arr3.count(0)==len(arr2):
                c+=1
        return c        
