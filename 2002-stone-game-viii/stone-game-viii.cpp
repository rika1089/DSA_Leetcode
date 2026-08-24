class Solution {
public:
    int n;
    vector<int> dp;
    int solve(vector<int>& pref, int idx) {
        if(idx >= n - 1)
            return pref[idx];
        if(dp[idx] != -1)
            return dp[idx];
        int take = pref[idx] - solve(pref, idx + 1);
        int skip = solve(pref, idx + 1);
        return dp[idx] = max(take, skip);
    }
    int stoneGameVIII(vector<int>& stones) {
        n = stones.size();

        vector<int> pref(n);
        dp.resize(n, 0);
        pref[0] = stones[0];
        for(int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + stones[i];
        }

        // return solve(pref, 1);
        dp[n - 1] = pref[n - 1];

        for(int i = n - 2; i >= 1; i--) {
            int take = pref[i] - dp[i + 1];
            int skip = dp[i + 1];
            dp[i] = max(take, skip);
        }

        return dp[1];


    }
};