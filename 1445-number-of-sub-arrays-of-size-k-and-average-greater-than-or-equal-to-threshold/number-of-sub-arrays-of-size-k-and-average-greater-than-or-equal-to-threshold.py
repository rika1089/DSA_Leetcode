class Solution:        
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        window_sum = sum(arr[:k])

        if window_sum / k >= threshold :
            cnt += 1
        
        for i in range(k,len(arr)) :
            window_sum += arr[i] - arr[i-k]
            if window_sum / k  >= threshold :
                cnt += 1

        return cnt


