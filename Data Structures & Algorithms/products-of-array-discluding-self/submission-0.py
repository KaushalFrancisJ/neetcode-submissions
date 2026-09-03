class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [1] * (len(nums)+1)
        

        for i in range(len(nums)-1, -1, -1):
            arr1[i] = (arr1[i+1]*nums[i])
        
        acc = 1

        result = [1] * (len(nums))

        for i in range(0, len(nums)):
            result[i] = acc * arr1[i+1]
            acc *= nums[i]
        return result
        