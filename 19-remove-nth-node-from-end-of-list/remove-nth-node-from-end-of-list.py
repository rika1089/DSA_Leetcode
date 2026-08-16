# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0

        # curr = head

        # while curr : 
        #     curr = curr.next 
        #     length += 1
        
        # if n == length :  # if list has 1 ele
        #     return head.next

        # length = length - n

        # curr = head # Again place the pointer to start

        # # Now start eliminating till you reach the elements index(length-n)

        # while length != 0 :
        #     # nxt = curr.next
        #     if length == 1 :
        #         curr.next = curr.next.next
        #         return head
            
        #     else :
        #         curr = curr.next
        #         length -= 1



        # Create a dummy node that points to the head
        # This helps handle edge cases like removing the first node
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, both starting at dummy
        slow = dummy
        fast = dummy

        # Move the fast pointer ahead by n+1 steps
        # This creates a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        # At that point, slow will be right before the node to delete
        while fast:
            slow = slow.next
            fast = fast.next

        # Skip the target node by adjusting the link
        slow.next = slow.next.next

        # Return the new head (dummy.next handles the case where head was removed)
        return dummy.next