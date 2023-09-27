class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start=ListNode(0)
        temp=start
        c=0
        while l1!=None or l2!=None:
            if l1!=None:
                num1=l1.val
            else:
                num1=0
            if l2!=None:
                num2=l2.val
            else:
                num2=0
            sum1=num1+num2+c
            d=sum1%10
            c=int(sum1/10)

            newn=ListNode(d)
            temp.next=newn
            temp=temp.next

            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next

        if l1==None and l2==None:
            if c!=0:
                newn=ListNode(c)
                temp.next=newn
                temp=temp.next

        start=start.next
        return start
