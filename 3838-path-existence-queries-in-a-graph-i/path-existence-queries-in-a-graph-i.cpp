class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // ############ BINARY SEARCH WILL NOT WORK HERE ############
        // int q = queries.size();
        // vector<bool> stats(q, false);
        // for(int i = 0; i < q; i++) {
        //     int src = queries[i][0], dst = queries[i][1];
        //     int low = min(src, dst), high = max(src, dst);
        //     int prev = low;
        //     bool flag = false;
        //     // for(int j = low; j <= high; j++) {
        //     //     if(abs(nums[prev] - nums[j]) > maxDiff)
        //     //         break;
        //     //     // cout << j << "->" << " " << abs(nums[prev] - nums[j]) << " |||| ";
        //     //     if(j == high) {
        //     //         flag = true;
        //     //         break;
        //     //     }
        //     //     prev = j;
        //     // }
        //     while(low < high) {
        //         mid = low + (high - low) / 2;
        //         if(abs(nums[mid] - nums[prev]) <= maxDiff) {
        //             if(mid == high) {
        //                 flag = true;
        //                 break;
        //             }
        //             low = mid + 1;
        //             prev = mid;
        //         }
        //         else 
        //     }
        //     if(flag)
        //         stats[i] = true;
        //     // cout << endl;
        // }
        // return stats;

        vector<int> reachable(n + 1, 0);
        int rank = 0;
        for(int i = 1; i < n; i++) {
            if(nums[i] - nums[i - 1] > maxDiff) {
                rank++;
            }
            reachable[i] = rank;
        }
        vector<bool> stats(queries.size(), false);
        for(int i = 0; i < queries.size(); i++) {
            if(reachable[queries[i][0]] == reachable[queries[i][1]]) {
                stats[i] = true;
            }
        }
        return stats;
    }
};