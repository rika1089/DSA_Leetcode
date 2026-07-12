class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)
        rankmap = {}
        rank = 1
        for num in nums :
            if num not in rankmap :
                rankmap[num] = rank
                rank += 1
        for i in range(len(arr)) :
            arr[i] = rankmap[arr[i]]
        return arr
        