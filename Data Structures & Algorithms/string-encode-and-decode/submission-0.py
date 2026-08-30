class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result
    def decode(self, s: str) -> List[str]:
        i = 0 
        result = []
        while i< len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            start = j+1
            end = start + length
            result.append(s[start:end])
            i = end
        return result
        
