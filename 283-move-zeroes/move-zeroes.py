class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0  # pointer for placing non-zero elements

        # Step 1: Move non-zero elements forward
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Step 2: Fill the rest with zeros
        for i in range(j, n):
            nums[i] = 0
