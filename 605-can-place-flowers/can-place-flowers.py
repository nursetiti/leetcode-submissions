class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if i==0 and len(flowerbed) > 1:
                if flowerbed[i] ==0 and flowerbed[i+1] == 0:
                    flowerbed[i] =1;
                    count +=1;
            elif i == 0 and len(flowerbed) == 0:
                flowerbed[i] = 1;
                count +=1;
            elif i != 0 and i != len(flowerbed) -1:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1;
                        count +=1;
            elif i == len(flowerbed) -1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] =1;
                    count +=1;
        print(count)
        if count >= n:
            return True
        else:
            return False


        