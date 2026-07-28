#this has been done by me.jasvanth.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=[]
        while list1 or list2:
            if list1:
                dummy.append(list1.val)
                list1=list1.next
            if list2:
                dummy.append(list2.val)
                list2=list2.next   
        dummy=sorted(dummy)
        head=None
        tail=None
        for i in dummy:
            newnode=ListNode(i)
            if head == None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
        return head

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna