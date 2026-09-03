class Solution:
    
    def encode(self, strs: List[str]) -> str:
        comb = ''.join(strs)
        metadata = {'len': len(comb), 'words': len(strs), 'chars' : []}
        for i in strs:
            metadata['chars'].append(str(len(i)))
        return f"{comb}::[{",".join(metadata['chars'])}]::{metadata['words']}::{metadata['len']}"
        
    def decode(self, s: str) -> List[str]:
        print(s)
        temp = s.split('::')
        length = int(temp[-1])
        words = int(temp[-2])
        if words == 0:
            return []
        chars = temp[-3][1:-1].split(',')
        comb = s[:length]
        strs = []
        startindex = 0
        for i in chars:
            i = int(i)
            strs.append(s[startindex:startindex+i])
            startindex += i
        return strs

