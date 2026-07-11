class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = [0]*(2*n)

        # for i in range(n) :
        #     ans[2*i] = nums[i]
        #     ans[2*i+1] = nums[i+n]

        # return ans
        x = nums[:n]
        y = nums[n:]
        z = []

        if len(x) == len(y) :
            for i in range(n) :
                z.append(x[i])
                z.append(y[i])

        return z