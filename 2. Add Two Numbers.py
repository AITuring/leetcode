# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=''
        num2=''
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        add=str(int(num1[::-1])+int(num2[::-1]))
        add=add[::-1]
        head=ListNode(add[0])
        answer=head
        for i in range(1,len(add)):
            node=ListNode(add[i])
            head.next=node
            head=head.next
        return answer

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        target=l1.val+l2.val
        res=ListNode.__init__(target % 10)
        res.next= self.addTwoNumbers2(l1.next, l2.next)
        if target>=10:
            res.next=self.addTwoNumbers2(res.next,)



