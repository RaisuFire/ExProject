# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        n = 1
        n = max(n , 1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        return n


if __name__ == "__main__":
    node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    so = Solution()
    print(so.maxDepth(node))
    