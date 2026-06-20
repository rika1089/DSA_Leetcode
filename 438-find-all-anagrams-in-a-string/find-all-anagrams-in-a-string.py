class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sorted_p = sorted(p)
        for i in range(len(s)-len(p)+1) :
            if sorted(s[i:i+len(p)]) == sorted_p :
                ans.append(i)

        return ans

                


        





