class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        bucket = set(nums)
        
        for i in bucket:
            if i - 1 not in bucket:
                curr = i
                acc = 1
                while curr + 1 in bucket:
                    curr += 1
                    acc += 1
                result = max(acc, result)
        return result