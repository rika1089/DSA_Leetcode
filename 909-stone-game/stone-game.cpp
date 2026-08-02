class Solution {
public:
    vector<vector<int>> dp;
    int solve(vector<int>& piles, int i, int j) {
        if(i > j)
            return 0;
        if(dp[i][j] != -1)
            return dp[i][j];
            
        int pi = piles[i] + min(solve(piles, i + 2, j), solve(piles, i + 1, j - 1));
        int pj = piles[j] + min(solve(piles, i, j - 2), solve(piles, i + 1, j - 1));
        
        return dp[i][j] = max(pi, pj);

    }
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        dp.resize(n, vector<int>(n, -1));
        int alice = solve(piles, 0, n - 1);
        int bob = accumulate(piles.begin(), piles.end(), 0) - alice;

        return alice > bob;

    }
};