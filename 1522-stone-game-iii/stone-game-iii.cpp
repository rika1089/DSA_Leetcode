class Solution {
public:
    int n;
    vector<int> dp;
    int solve(int idx, vector<int>& stoneValue) {
        if(idx >= n)
            return 0;
        if(dp[idx] != INT_MIN)
            return dp[idx];
        int res = INT_MIN;
        res = max(res, stoneValue[idx] - solve(idx + 1, stoneValue));
        if(idx + 1 < n)
            res = max(res, (stoneValue[idx] + stoneValue[idx + 1]) - solve(idx + 2, stoneValue));
        if(idx + 2 < n)
            res = max(res, (stoneValue[idx] + stoneValue[idx + 1] + stoneValue[idx + 2]) - solve(idx + 3, stoneValue));
        return dp[idx] = res;

    }
    string stoneGameIII(vector<int>& stoneValue) {
        n = stoneValue.size();
        dp.resize(n, INT_MIN);
        int base = solve(0, stoneValue);
        if(base > 0)
            return "Alice";
        else if(base == 0)
            return "Tie";
        return "Bob";
    }
};