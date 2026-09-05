from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        wordCommon = gcd(len(str1), len(str2))
        if str1 + str2 != str2 + str1:
            return ""
        
        newWord =[]
        for i in range(wordCommon):
            newWord.append(str1[i])
        
        newWord = "".join(newWord)
        return newWord