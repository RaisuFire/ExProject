# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        if t1 is None and t2 is None:
            return None

        node = TreeNode(t1.val+t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node

if __name__ == "__main__":
    node1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    node2 = TreeNode(2, TreeNode(1,None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    so = Solution()
    c = so.mergeTrees(node1, node2)
    print(c.val)
