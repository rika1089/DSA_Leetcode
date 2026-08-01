class Solution:
    def predictTheWinner(self, A: List[int]) -> bool:
        # Recursion | Memoaization
        
        n = len(A)
        if ~n & 1: return True

        @cache
        def maxDiff(i: int, j: int) -> int:
            if i == j: return A[i]
            return max(A[i] - maxDiff(i + 1, j),
                       A[j] - maxDiff(i, j - 1))

        return maxDiff(0, n - 1) >= 0

        # Bottom-Up DP | Space- Optimized

        # n = len(A)
        # if ~n & 1: return True

        # dp = [0] * n

        # for i in range(n - 1, -1, -1):
        #     dp[i] = A[i]
        #     for j in range(i + 1, n):
        #         dp[j] = max(A[i] - dp[j], A[j] - dp[j - 1])

        # return dp[n - 1] >= 0