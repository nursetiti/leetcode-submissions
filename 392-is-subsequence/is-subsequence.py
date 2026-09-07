class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        piv = 0
        count = 0;
        for i in(t):
            if piv < len(s) and i == s[piv]:
                count +=1;
                piv +=1;
        if count == len(s):
            print(count)
            return True
        else:
            return False