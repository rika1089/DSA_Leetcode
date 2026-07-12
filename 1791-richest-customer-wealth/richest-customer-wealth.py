class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0

        for person in accounts :
            ans = max(ans,sum(person))

        return ans