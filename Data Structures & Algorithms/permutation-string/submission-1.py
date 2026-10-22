import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = defaultdict(int)
        for i in s1:
            letters[i] += 1

        for i in range(len(s2)):
            j = i
            currentLetters = copy.deepcopy(letters)
            while j<len(s2) and currentLetters[s2[j]] > 0:
                currentLetters[s2[j]] -= 1
                j+=1
            if j-i == len(s1):
                return True
            if i < j:
                i = j-1
        return False