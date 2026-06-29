class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for s in patterns : 
            if s in word :
                cnt += 1
        
        return cnt