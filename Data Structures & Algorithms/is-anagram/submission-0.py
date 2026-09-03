class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in s:
            charDict[i] += 1
        for j in t:
            if charDict[j] == 0:
                return False
            charDict[j] -= 1
        return True
        