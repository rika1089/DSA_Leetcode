class Solution:
    def issorted(self,nums : List[int]) -> bool :
        for i in range(len(nums)-1) :
            if nums[i] > nums[i+1] :
                return False
        return True

    def rotate(self,nums:List[int],d : int) -> nums :
        nums = nums[-d:] + nums[:-d]
        return nums


    def check(self, nums: List[int]) -> bool:
        d = len(nums)

        for i in range(len(nums)) :
            if self.issorted(self.rotate(nums,i)) :
                return True
        return False


        