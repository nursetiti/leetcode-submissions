class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = 0;
        pref = 0;
        for i in range(len(gain)):
            pref += gain[i]

            if pref > highest:
                highest = pref
        return highest 
        