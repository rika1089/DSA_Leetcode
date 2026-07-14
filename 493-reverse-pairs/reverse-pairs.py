class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge_sort(left: List[int],right: List[int]) -> int :
            if left >= right :
                return 0
            
            mid = ( left + right ) // 2
            count = merge_sort(left,mid) + merge_sort(mid+1, right)

            i = left
            j = mid + 1

            # Count reverse pairs in the respetive halves :
            for i in range(left,mid + 1) :
                while j <= right and nums[i] > 2 * nums[j] :
                    j +=1
                
                count += j-(mid+1)

            # Merge the two sorted halves
            temp = []
            i,j = left,mid+1

            while i <= mid and j <= right :
                if nums[i] <= nums[j] :
                    temp.append(nums[i])
                    i += 1
                else :
                    temp.append(nums[j])
                    j += 1

            # Add remaining elements(if any) too to the temp
            while i <= mid :
                temp.append(nums[i])
                i += 1
            while j <= right :
                temp.append(nums[j])
                j += 1

            # Insert those numbers back into original nums from temp

            nums[left:right+1] = temp
            return count 

        return merge_sort(0,len(nums)-1)
            


                