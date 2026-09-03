class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictDb = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            dictDb[key].append(i)
        return list(dictDb.values())
        