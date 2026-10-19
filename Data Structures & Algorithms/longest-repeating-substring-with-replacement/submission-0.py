from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        maxfreq = 0

        l = r = 0

        while r < len(s):
            
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])
            while r-l+1 - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
            r += 1
        
        return result
            
