# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    s = []
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

    #Recursion:
    """
        if not root:
            return False
        elif not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    """
    #DFS:
    """
    if not root:
            return False
    stack = [(root,sum - root.val)]
    while stack:
        u = stack.pop()
        if not u[0].left and not u[0].right:
            if u[1] == 0:
                return True
        if u[0].left:
            stack.append((u[0].left, u[1]-u[0].left.val))
        if u[0].right:
            stack.append((u[0].right, u[1]-u[0].right.val))
    return False
    """

if __name__ == "__main__":
    node = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4)))
    sum = 22
    so = Solution()
    c = so.hasPathSum(node, sum)
    print(c)
