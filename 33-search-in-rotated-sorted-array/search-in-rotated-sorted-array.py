class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i,val in enumerate(nums) :
            if val == target :
                return i

        return -1
        