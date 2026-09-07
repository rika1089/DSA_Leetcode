class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2 :
            return None
        
        # res = [-1]*n1

        # for i in range(n1) :
        #     pos = nums2.index(nums1[i])
        #     j = pos + 1
        #     if nums1[i] in nums2 :
        #         while j < n2 :
        #             if nums1[i] < nums2[j] :
        #                 res[i] = nums2[j]
        #                 break
        #             j += 1
        # return res
        hmap = {}
        stack = []

        for num in nums2 :
            while stack and num > stack[-1] :
                popped = stack.pop()
                hmap[popped] = num
            stack.append(num)

        res = []
        for num in nums1 :
            if num in hmap :
                res.append(hmap[num])
            else :
                res.append(-1)
        return res




