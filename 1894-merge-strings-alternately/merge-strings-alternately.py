class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged =[]
        # notInList=[]

        for i, char1 in enumerate(word1):
            for j, char2 in enumerate(word2):
                if i==j:
                    merged.append(char1) 
                    merged.append(char2)
        if len(word1) > len(word2):
            merged.extend(word1[len(word2):])
        elif len(word2) > len(word1):
            merged.extend(word2[len(word1):])
        
        merged ="".join(merged)
        return merged
    