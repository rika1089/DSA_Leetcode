class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        n = len(gain)
        for g in gain :
            alt.append(alt[-1]+g)

        return max(alt)
        