# Definition for a binary tree node.
import operator
from collections import deque
from filecmp import cmp
# from queue import Queue
import queue


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and self.isSymmetricTree(node1.left, node2.right) and self.isSymmetricTree(
                node1.right, node2.left)
        else:
            return node1 == node2


if __name__ == "__main__":
    node = TreeNode(1, (TreeNode(2, TreeNode(3), TreeNode(4))), (TreeNode(2, TreeNode(4), TreeNode(3))), )
    node = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    so = Solution()
    l = so.isSymmetric(node)
    print(l)

