# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False

        def cycle(root1,root2):
            if root1==None or root2==None or root2.next==None:
                return False
            if root1==root2:
                return True
            return cycle(root1.next,root2.next.next)
        
        return cycle(head,head.next)