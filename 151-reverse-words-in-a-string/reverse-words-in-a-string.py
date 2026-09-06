class Solution:
    def reverseWords(self, s: str) -> str:
        splittedWord = s.split()
        splitteds = splittedWord.copy()

        for i in range(len(splittedWord)):
            splittedWord[i] = splitteds.pop()

        splittedWord = " ".join(splittedWord)
        return splittedWord
            # i.append(reversedWord)

        