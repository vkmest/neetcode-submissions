# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        
        def travel(node1, node2):
            if (node1 == None and node2 != None) or (node1 != None and node2 == None):
                return False
            
            if node1 == None and node2 == None:
                return True
            
            if node1.val != node2.val:
                return False

            # node1.val == node2.val:
            return travel(node1.left, node2.left) and travel(node1.right, node2.right)
        
        def SubTree(node, subNode):
            check = travel(node, subNode)
            if check:
                self.found = True
            if node:
                SubTree(node.left, subNode)
                SubTree(node.right, subNode)
        
        SubTree(root, subRoot)
        return self.found