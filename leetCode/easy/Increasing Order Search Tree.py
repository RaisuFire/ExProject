# Definition for a binary tree node.
from heapq import heappush, heappop


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# def append_right(node, data):
#     if node.right is None:
#         node.right = TreeNode(data)
#         return
#     else:
#         append_right(node.right, data)


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if root is None:
        #     return
        # stack = [root]
        # heap = []
        # while stack:
        #     temp = stack.pop()
        #     heappush(heap, temp.val)
        #     if temp.left is not None:
        #         stack.append(temp.left)
        #     if temp.right is not None:
        #         stack.append(temp.right)
        #
        # ans = []
        # for i in range(len(heap)):
        #     ans.append(heappop(heap))
        #     ans.append(None)
        # return ans[:-1]

        if not root:
            return None
            # get inorder list
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        # adjust node.right
        dummy = pre = TreeNode(-1)
        i = 0
        while i < len(res):
            pre.right = TreeNode(res[i])
            print("pre.right:", pre.right.val)
            print("dummy.right", dummy.right.val)
            pre = pre.right
            print("preval:", pre.val)
            # print("dummy.right", dummy.right.val)
            i += 1
        return dummy.right

if __name__ == "__main__":
    node = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                    TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
    # node = TreeNode(379, TreeNode(826))
    so = Solution()
    c = so.increasingBST(node)
    # print(c)
