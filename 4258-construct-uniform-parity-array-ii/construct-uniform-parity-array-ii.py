class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if not nums1 :
            return True

        nums = sorted(nums1)

        minele_parity = nums[0] & 1 

        # let seen[0] = even seen[1] = odd
        seen = [False, False]

        # lets assume smallest ele as seen
        seen[minele_parity] = True

        for x in nums[1:] :
            p = x & 1 
            if p == minele_parity :
                seen[p] = True
                continue
            
            # need a small with parity = p XOR minele_parity
            required = p ^ minele_parity

            if not seen[required] :
                return False
            
            
            seen[p] = True

        return True