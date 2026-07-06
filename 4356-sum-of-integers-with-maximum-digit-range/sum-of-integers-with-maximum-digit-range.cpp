class Solution {
public:
    int getRange(int num) {
        int mxD = INT_MIN, mnD = INT_MAX;
        while(num) {
            mxD = max(mxD, num % 10);
            mnD = min(mnD, num % 10);
            num /= 10;
        }
        return mxD - mnD;
    } 
    int maxDigitRange(vector<int>& nums) {
        int maxRange = 0, range;
        vector<int> ranges;
        for(int i = 0; i < nums.size(); i++) {
            range = getRange(nums[i]);
            maxRange = max(maxRange, range);
            ranges.push_back(range);
        }
        int sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(maxRange == ranges[i])
                sum += nums[i];
        }
        return sum;
    }
};