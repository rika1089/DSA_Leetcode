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



        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:

            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next