class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        initialCommonPrefix = strs[0]
        for word in strs[1:]:
            lenOfprefix = 0;
            print(word)
            lenOfWord = len(word)
            lenOfPrefix = len(initialCommonPrefix)
            for i in range(min(lenOfWord, lenOfPrefix)):
                if initialCommonPrefix[i] == word[i]:
                    lenOfprefix +=1;
                else:
                    break

            initialCommonPrefix = initialCommonPrefix[:lenOfprefix]
        return initialCommonPrefix
            


        