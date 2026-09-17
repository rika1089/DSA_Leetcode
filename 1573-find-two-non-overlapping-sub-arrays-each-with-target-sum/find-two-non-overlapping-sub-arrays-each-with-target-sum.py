class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int :
                                                        # TC = O(n)  : iterating once
                                                        # SC = O(n)  : for 1D dp
        n = len(arr)
        ans = n + 1 
        total = 0
        i = 0
        dp = [n] * (n+1)  # dp[j] : min len of valid subarray ending before j
        for j in range(n) :
            total += arr[j]

            # Move right while sum < k   -> expand
            # Move down while sum > k    -> Shrink
            while total > target :  
                total -= arr[i]
                i += 1
            
            dp[j+1] = dp[j]

            # If target sum is found
            if total == target :
                Len = j-i+1  # Cal Len
                ans = min(ans,Len+dp[i])  # Since we need to have min length of valid subarrays
                dp[j+1] = min(dp[j],Len)  # update min len of valid subarray 
        
        # If no suck pair is found 
        if ans == n + 1 :
            return -1
        else : 
            return ans