# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Find Middle 
        slow,fast = head,head 
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        # 2 . Reverse the second half

        prev,curr = None,slow.next
        slow.next = None
        while curr :
            new = curr.next
            curr.next = prev
            prev,curr = curr,new
        # return prev

        # Merge 1st half , (reversed) 2nd half : one by one from each 
        # Step 3: Merge two halves
        first, second = head, prev   # 'first' starts at the head of the first half,
                                    # 'second' starts at the head of the reversed second half

        while second:                # keep going until we've merged all nodes from the second half
            tmp1, tmp2 = first.next, second.next   # save the next pointers before overwriting
                                                # tmp1 = next node in first half
                                                # tmp2 = next node in second half

            first.next = second      # link current node from first half → current node from second half
            second.next = tmp1       # link current node from second half → next node in first half

            first, second = tmp1, tmp2   # advance both pointers forward
                                        # move 'first' to its saved next (tmp1)
                                        # move 'second' to its saved next (tmp2)
