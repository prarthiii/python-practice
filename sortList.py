class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):   
        current = head
        while current and current.next: 
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        print(head)



n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

sol = Solution()
print(sol.deleteDuplicates(n1))