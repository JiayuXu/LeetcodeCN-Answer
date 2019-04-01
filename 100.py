# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None and q!=None:
            return False
        if p!=None and q==None:
            return False
        if p.val==q.val:
            s1=self.isSameTree(p.left,q.left)
            s2=self.isSameTree(p.right,q.right)
            if s1 and s2:
                return True
            else:
                return False
        else:
            return False
