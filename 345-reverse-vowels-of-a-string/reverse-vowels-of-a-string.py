class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelStore =[]
        s = list(s)
        for i in s:
            if i.lower() in vowels:
                vowelStore.append(i)
        # vowelStore.reverse()
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = vowelStore.pop()
                # vowelStore.pop()
        s = "".join(s)
        return s

        