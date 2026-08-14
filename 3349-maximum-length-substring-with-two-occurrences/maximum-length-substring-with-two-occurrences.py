class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        maxi = float('-inf')
        for i in range(n) :
            for j in range(i+1 , n) :
                substr = s[i:j+1]
                frequency = {}
                for char in substr :
                    frequency[char] = frequency.get(char , 0) + 1

                if all(freq <= 2 for freq in frequency.values()) :
                    maxi = max(maxi , len(substr))
        return maxi

