class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c1map = {}
        c2map = {}
        for i in range(len(s)) :
            if s[i] in c1map and c1map[s[i]] != t[i] :
                return False
            if t[i] in c2map and c2map[t[i]] != s[i] :
                return False
            c1map[s[i]] = t[i]
            c2map[t[i]] = s[i]        
        return True


        