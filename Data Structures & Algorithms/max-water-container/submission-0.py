class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        result = 0
        while i<j:
            anchor = min(heights[i], heights[j])
            result = max(result, anchor*(j-i))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return result