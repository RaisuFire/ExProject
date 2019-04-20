# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """



        def leavesnums(root, s):
            if root is None:
                return
            if root.left is None and root.right is None:
                s.append(root.val)
            if root.left:
                leavesnums(root.left, s)
            if root.right:
                leavesnums(root.right, s)
            return s

        return leavesnums(root1, []) == leavesnums(root2, [])
        # r1 = leavesnums(root1, [])
        # r2 = leavesnums(root2, [])
        # return r1 == r2

"""
def iterative(self,root,s):
    if root is not None:
        stack = []
        stack.append(root)
        while stack:
            x = stack.pop(-1)
            if x.left is None and x.right is None:
                s.append(x.val)
                continue
            if x.right is not None:
                stack.append(x.right)
            if x.left is not None:
                stack.append(x.left)
    return s
"""


if __name__ == '__main__':
    # node1 = TreeNode(1, TreeNode(2,TreeNode(3), TreeNode(4)), TreeNode(5))
    # node2 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    # so = Solution()
    # r = so.leafSimilar(node1, node2)
    # print(r)
    s = [1, 2, 3]
    c = s.pop(-1)
    print(c)