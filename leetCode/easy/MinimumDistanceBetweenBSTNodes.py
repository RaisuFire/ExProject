# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res


if __name__ == "__main__":
    node = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    so = Solution()
    r = so.minDiffInBST(node)
    print(r)
