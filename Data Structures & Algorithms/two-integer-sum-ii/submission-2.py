class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        db = defaultdict(int)

        for i in range(len(numbers)):
            reqNum = target - numbers[i]
            if reqNum in db:
                return [db[reqNum]+1, i+1]
            db[numbers[i]] = i
        return [0,0]