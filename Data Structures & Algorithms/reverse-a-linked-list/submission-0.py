# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode()
        new_head_start=new_head
        def dfs(root):
            nonlocal new_head
            if not root:
                return
            if root.next==None:
                new_head.next=root
                new_head=new_head.next
                return
            else:
                dfs(root.next)
            new_head.next=root
            new_head=new_head.next
            
        dfs(head)
        new_head.next=None
        return new_head_start.next