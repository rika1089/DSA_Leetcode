class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for ind,char in enumerate(s) :
            res += (ord('z')-ord(char)+1) * (ind+1)
        
        return res