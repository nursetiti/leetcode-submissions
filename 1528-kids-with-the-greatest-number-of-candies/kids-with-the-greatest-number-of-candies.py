class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest =[]
        candiesNew = candies.copy()
        for i in range(len(candiesNew)):
            candiesNew[i] = candiesNew[i] + extraCandies
            if max(candiesNew) == candiesNew[i]:
                greatest.append(True)
            else:
                greatest.append(False)
            candiesNew = candies.copy()
        return greatest
