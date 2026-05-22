class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=0;
        maxN =0;
        for i in (nums):
            if i==1:
                n +=1;
                if n>maxN:
                    maxN =n;
            else:
                n = 0;
        return maxN;
            