# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = True #A flag to know when to quit the loop
        plusdigit = 0
        node = ListNode()
        return_node = node
        while(flag):
            #Assume that at least one linked lists have not been exhausted.
            if l1 == None:
                digit = l2.val + plusdigit
            elif l2 == None:
                digit = l1.val + plusdigit
            else:
                digit = l1.val + l2.val + plusdigit
            
            if digit >= 10:
                plusdigit = digit // 10 #integer division
                digit = digit % 10
            else:
                plusdigit = 0
            
            #Update node.
            node.val = digit

            #Move on with l1 and l2 as well.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            #Check exit condition: both
            if l1 == None and l2 == None:
                flag = False
                # If there is an overflow digit, add it.
                if plusdigit is not 0:
                    node.next = ListNode(val=plusdigit)
            # Create next node if there should be a next node.
            else:
                node.next = ListNode()
                node = node.next
        return return_node