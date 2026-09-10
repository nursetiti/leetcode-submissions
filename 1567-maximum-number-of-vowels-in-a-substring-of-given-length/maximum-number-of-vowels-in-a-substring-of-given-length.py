class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        left = 0
        right = k

        currentWindow = s[left:right]

        count = 0

        for char in currentWindow:
            if char in vowels:
                count += 1

        maxVowels = count

        while right < len(s):

            # remove the character leaving
            if s[left] in vowels:
                count -= 1

            # add the character entering
            if s[right] in vowels:
                count += 1

            left += 1
            right += 1

            if count > maxVowels:
                maxVowels = count

        return maxVowels