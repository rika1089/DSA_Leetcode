class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        # Equal parity produce and "even" number as diff
        # DIff parity produce and "odd" number as diff
        #  E - E = E            O - O = E
        #  E - O = O            O - E = O

        # so however only even or odd are produced which satisfy the given question
        # Therefore, we simply return true.
        return True