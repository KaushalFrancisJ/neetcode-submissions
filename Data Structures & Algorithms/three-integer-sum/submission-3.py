class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0

        result =[]
        dedup = set()

        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                if target > nums[j] + nums[k]:
                    j+=1
                elif target < nums[j] + nums[k]:
                    k-=1
                else:
                    if (nums[i], nums[j], nums[k]) not in dedup:
                        result.append([nums[i], nums[j], nums[k]])
                        dedup.add((nums[i], nums[j], nums[k]))
                    k-=1
                    j+=1
                    
        
        return result
                