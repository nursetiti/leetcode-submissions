class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelStore =[]
        s = list(s)
        for i in s:
            if i in vowels:
                vowelStore.append(i)
        print(vowelStore)
        vowelStore.reverse()
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowelStore[0]
                del vowelStore[0]
        s = "".join(s)
        return s

        