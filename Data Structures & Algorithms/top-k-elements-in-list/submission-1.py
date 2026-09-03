class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsfreq = defaultdict(int)
        for i in nums:
            numsfreq[i] += 1
        freqnums = defaultdict(list)
        for key, value in numsfreq.items():
            freqnums[value].append(key)
        
        result = []
        for i in range(len(nums), 0, -1):
            if i in freqnums:
                result.extend(freqnums[i])
                if len(result) >= k:
                    return result[:k]
        return result[:k]