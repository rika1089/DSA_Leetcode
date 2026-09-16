MOD = 10 ** 9 + 7
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # return math.comb(n+k-1, 2*k) % MOD
        dp = [1] * n
        prefix_sums = [0] * (n + 1)
        for j in range(n):
            prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % MOD
        for _ in range(k):
            dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix_sums[j]) % MOD
            for j in range(n):
                prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % MOD
        return dp[n - 1]