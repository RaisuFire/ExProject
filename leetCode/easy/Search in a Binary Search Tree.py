# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return
        stack = [root]
        while stack:
            n = stack.pop()
            if n is None:
                continue
            if n.val == val:
                return n
            stack.append(n.left)
            stack.append(n.right)


if __name__ == "__main__":
    node = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    so = Solution()
    val = 2
    c = so.searchBST(node, val)
    print(c.val)
