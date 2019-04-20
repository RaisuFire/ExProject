# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    # n = []
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # n = 0
        # if root is None:
        #     return
        # if root.left is not None:
        #     n += root.left.val
        # self.sumOfLeftLeaves(root.left)
        # self.sumOfLeftLeaves(root.right)
        # return n

        if not root:
            return 0
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node.left:
                # This determine if the node.left is a left leave
                if not node.left.left and not node.left.right:
                    res.append(node.left.val)
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


        # sum = 0
        # if not root:
        #     return 0
        # if root.left and not root.left.left and not root.left.right:
        #     sum += root.left.val
        # sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        # return sum


if __name__ == "__main__":
    node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # node = TreeNode(1)
    so = Solution()
    c = so.sumOfLeftLeaves(node)
    print(c)
