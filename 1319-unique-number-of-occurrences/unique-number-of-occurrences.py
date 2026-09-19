class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr2 = set(arr)
        countSet =set()
        for i in (arr2):
            count = arr.count(i)
            print(i, count)
            if count in countSet:
                return False
            countSet.add(count)
        return True