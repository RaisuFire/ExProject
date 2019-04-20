# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "({} {} {})".format(self.val, self.left, self.right)


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        if L <= root.val <= R:
            # print(root)
            return root
        if root.val < L:
            # print("right", root)
            return root.right
        if root.val > R:
            # print("left", root)
            return root.left


if __name__ == '__main__':
    # node = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
    node = TreeNode(1, TreeNode(0), TreeNode(2))
    l, r = 1, 3
    so = Solution()
    c = so.trimBST(node, l, r)
    print(c)
