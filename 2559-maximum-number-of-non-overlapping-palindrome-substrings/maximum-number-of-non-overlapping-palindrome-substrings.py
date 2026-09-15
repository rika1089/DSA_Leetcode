class Solution:
    def ispalindrome(self,s:str) -> bool :
        l = 0
        r = len(s)-1
        while l <= r :
            if s[l] != s[r] :
                return False
            l += 1
            r -= 1
        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1 :         # Every char in string is a palindrome
            return len(s)
        n = len(s)
        cnt = 0
        i = 0

        while i <= n - k : # The last index will be covered by other pointer
            found = False
            for j in (k,k+1) : # Since we only need to check len > k. so, {k,k+1} enough 
                if i+j <= n and self.ispalindrome(s[i:i+j]) :
                    cnt += 1
                    found = True
                    i += j  # Since not overlapping the next index start from j
                    break
            if not found :
                i += 1
        return cnt
                    
                

        