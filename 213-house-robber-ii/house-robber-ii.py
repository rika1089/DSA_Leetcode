class Solution:
    def rob(self, nums: List[int]) -> int:
        House_robber_II_memo0 = {}
        House_robber_II_memo1 = {}
        if len(nums) == 1:
            return nums[0]
        def House_Robber_II(i , nums , House_robber_II_memo) :

            # Use of memoization 
            if i in House_robber_II_memo :
                return House_robber_II_memo[i]

            # BAse Case
            if i >= len(nums) :
                return 0

            # Dynamic Programming         
            rob = nums[i] + House_Robber_II(i+2, nums,House_robber_II_memo) # Jump two steps since i+1 is adjacent
            notrob = House_Robber_II(i+1, nums, House_robber_II_memo)

            # Feed Memoization
            House_robber_II_memo[i] = max(rob , notrob)

            return House_robber_II_memo[i]

        return max(House_Robber_II(0,nums[:-1],House_robber_II_memo0), House_Robber_II(1,nums,House_robber_II_memo1))