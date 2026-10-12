class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        l = r = 0
        result = 0

        while (r<len(s) and l<=r):
            if s[r] not in cache:
                cache.add(s[r])
                result = max(result, r-l+1)
                r+=1
            else:
                cache.remove(s[l])
                l+=1
        
        return result
        
        
