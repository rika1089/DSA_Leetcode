class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return (nums[-1]-1)*(nums[-2]-1)
        max1 = float('-inf')
        max2 = float('-inf')

        for num in nums :
            if num >= max1 :
                max2 = max1
                max1 = num
                
            elif  num >= max2 :
                max2 = num

        return (max1-1)*(max2-1)