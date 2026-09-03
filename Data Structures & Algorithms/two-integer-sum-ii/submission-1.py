class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        db = defaultdict(list)
        for i in range(len(numbers)):
            reqNum = target - numbers[i]
            if reqNum in db:
                return [db[reqNum][0]+1, i+1]
            db[numbers[i]].append(i)
        
        return [0,0]



        