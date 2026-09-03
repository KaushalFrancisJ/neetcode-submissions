class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valInd = {}
        for i in range(len(nums)):
            if valInd.get(target-nums[i]) is not None:
                return [valInd.get(target-nums[i]), i]
            valInd[nums[i]] = i
        return [-1, -1]
