class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #First find the breaking point
        ind = -1
        n = len(nums)
        for i in range(n-2,-1,-1) :
            if nums[i] < nums[i+1] :
                ind = i
                break

        # if no breaking pt present 
        if ind == -1 :
            nums.reverse()
            return 

        # after finding the index swap it with the smallest in the remaining part of the array

        for i in range(n-1,ind,-1) :
            if nums[i] > nums[ind] :
                nums[i],nums[ind] = nums[ind],nums[i]
                break

        # reverse the rest of the array 
        nums[ind+1:] = reversed(nums[ind+1:])

     