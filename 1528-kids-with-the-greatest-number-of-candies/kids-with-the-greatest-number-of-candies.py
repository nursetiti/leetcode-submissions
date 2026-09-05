class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest =[]
        candiesNew = candies.copy()
        for i in range(len(candiesNew)):
            candiesNew[i] = candiesNew[i] + extraCandies
            if max(candiesNew) == candiesNew[i]:
                greatest.append(True)
            elif max(candiesNew) != candiesNew[i]:
                greatest.append(False)
            candiesNew = candies.copy()
        return greatest

        # print(extraCandies)
        # candiesNew = candies
        # for i in candiesNew:
        #     posI = candiesNew.index(i)
        #     i = i + extraCandies
        #     candiesNew[posI] = i
        #     print(candiesNew)
        # candiesNew = candies