class Solution:
    MOD = 10 ** 9 + 7
    def distinctSubseqII(self, s: str) -> int:
        totalsubseq = 0
        dp = [0] * 26

        for char in s :
            char = ord(char) - ord('z')
            new = totalsubseq + 1 - dp[char]
            totalsubseq = (totalsubseq + new) % self.MOD
            dp[char] = (dp[char] + new) % self.MOD
        
        return totalsubseq
        