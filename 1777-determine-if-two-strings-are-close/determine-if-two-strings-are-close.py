class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        count1 = {}
        count2 = {}

        # Count characters in word1
        for char in word1:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1

        # Count characters in word2
        for char in word2:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        if set(count1.keys()) != set(count2.keys()):
            return False

        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True