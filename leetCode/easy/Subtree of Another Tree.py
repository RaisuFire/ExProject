class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s,t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and isSame(s.left,t.left) and isSame(s.right,t.right)

        def traverse(s, t):
            if not s and not t:
                return True
            elif not s and t:
                return False
            elif s and not t:
                return False
            else:
                if s.val != t.val:
                    return traverse(s.left, t) or traverse(s.right, t)
                else:
                    if traverse(s.left, t) or traverse(s.right, t):
                        return True
                    else:
                        return isSame(s, t)

        return traverse(s, t)



    s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    t = TreeNode(4, TreeNode(1), TreeNode(5))
    so = Solution()
    a = so.isSubtree(s, t)
    print(a)

