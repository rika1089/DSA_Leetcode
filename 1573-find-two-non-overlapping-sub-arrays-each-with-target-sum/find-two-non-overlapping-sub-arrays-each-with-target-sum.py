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

        # TLE
                                       # TC = O(n^2)  : iterating once
                                       # SC = O(len(subs)^2)  : for dp                                   
        # n = len(arr)
        # subs = []
        # # find all subarrays with sum == target
        # for i in range(n):
        #     s = 0
        #     for j in range(i, n):
        #         s += arr[j]
        #         if s == target:
        #             subs.append((i, j, j - i + 1))  # (start, end, length)

        # ans = float('inf')
        # # check all pairs for non-overlap
        # for i in range(len(subs)):
        #     for j in range(i + 1, len(subs)):
        #         s1, e1, l1 = subs[i]
        #         s2, e2, l2 = subs[j]
        #         if e1 < s2 or e2 < s1:  # non-overlapping
        #             ans = min(ans, l1 + l2)

        # return ans if ans != float('inf') else -1
