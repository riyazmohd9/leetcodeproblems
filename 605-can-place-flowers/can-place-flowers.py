class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0:
                # Add len(flowerbed) == 1 check so it doesn't look for an index that isn't there
                if flowerbed[i] == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n-=1
            elif flowerbed[i]==0 and flowerbed[i+1] == 0 and flowerbed[i-1] ==0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
