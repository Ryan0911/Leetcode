# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, node2):
    if(node.val != node2.val):
        return False
    if(node.val == node2.val):
        dfs(node.left, node2.left)
        dfs(node2.rigt, node2.right)


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if(dfs(p, q) == False):
            return False
        return True
