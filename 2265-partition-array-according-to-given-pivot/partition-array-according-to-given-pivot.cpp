class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        // normie
        int n = nums.size(), cnt = 0;
        // 9 5 3
        // 10 10
        // 12 14
        vector<int> res;
        vector<int> left, right;

        for(int i = 0; i < n; i++) {
            if(nums[i] < pivot)
                left.push_back(nums[i]);
            else if(nums[i] > pivot)
                right.push_back(nums[i]);
            else
                cnt++;
        }

        for(int i = 0; i < left.size(); i++)
            res.push_back(left[i]);
        for(int i = 0; i < cnt; i++)
            res.push_back(pivot);
        for(int i = 0; i < right.size(); i++)
            res.push_back(right[i]);
        
        return res;
    }
};