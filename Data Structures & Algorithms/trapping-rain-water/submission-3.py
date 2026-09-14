class Solution:
    def trap(self, height: List[int]) -> int:
        premax = height.copy()
        sufmax = height.copy()
        result = 0
        for i in range(1, len(height)):
            if premax[i-1] > premax[i]:
                premax[i] = premax[i-1]
        
        for i in range(len(height)-2, -1, -1):
            if sufmax[i+1] > sufmax[i]:
                sufmax[i] = sufmax[i+1]
        
        for i in range(len(height)):
            result += min(premax[i], sufmax[i]) - height[i]
        return result
