#This has been done by me.Jasvanth.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1,sum2=0,0
        copy1=l1
        copy2=l2
        while l1 or l2:
            if l1 :
                sum1=sum1*10+l1.val
                l1=l1.next
            if l2 :
                sum2=sum2*10+l2.val
                l2=l2.next
        
        rev1,rev2=str(sum1),str(sum2)
        rev1,rev2=int(rev1[::-1]),int(rev2[::-1])
        while copy1.val==0 and copy1.next:
            rev1=rev1*10
            copy1=copy1.next
        while copy2.val==0 and copy2.next:
            rev2=rev2*10
            copy2=copy2.next

        result=rev1+rev2
        print(result,type(result))
        if result==0:
            return ListNode(0)
        head=None
        Current=None
        while result>0:
            a=result%10
            newnode=ListNode(a)
            if head==None:
                head=newnode
                current=newnode
            else:
                current.next=newnode
                current=newnode
            result=result//10
        return head





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna