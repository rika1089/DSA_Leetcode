class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(str(n).strip())
        n.sort()
        if len(n) >= 2 :
            return int(n[-1]) * int(n[-2])