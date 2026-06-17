
class Solution:
    def frequencySort(self, s: str) -> str:
        Map = {}
        for ch in s :
            if ch not in Map :
                Map[ch] = 1
            else :
                Map[ch] += 1
            
        Map = sorted(Map.items(),key=lambda x : x[1],reverse = True)
        ans = ''
        for key,val in Map:
            ans += key*val
        
        return ans

        