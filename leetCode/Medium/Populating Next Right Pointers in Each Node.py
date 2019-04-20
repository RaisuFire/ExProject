# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x, left=None, right=None, next=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next
from collections import deque


class Solution:
    # @param root, a tree link node
    # @return nothing
    # def connect(self, root):
    #     if root is None:
    #         return
    #     stack = [root]
    #     while len(stack) > 0:
    #         n = stack.pop(0)
    #         pre = n
    #         print(n.val)
    #         if n.left is not None:
    #             stack.append(n.left)
    #         if n.right is not None:
    #             stack.append(n.right)
    def connect(self, root):
        """
        BFS on binary search tree connecting each node to the next node
        """
        if not root:
            return

            # Create a deque for level being processed
        stack = deque([root])
        # Temp holder for level
        level = []

        while stack:
            # Grab the furthest left item on the stack
            cur = stack.popleft()

            # Add right reference, next node on stack is the node to the right
            if stack:
                cur.next = stack[0]

            # Add Children next level to process
            if cur.left:
                level.append(cur.left)
            if cur.right:
                level.append(cur.right)

            if not stack and level:
                # Add next level to process and clear temp level
                stack.extend(level)
                level = []


if __name__ == "__main__":
    node1 = TreeLinkNode(1, TreeLinkNode(2, TreeLinkNode(4), TreeLinkNode(5)),
                         TreeLinkNode(3, TreeLinkNode(6), TreeLinkNode(7)))
    so = Solution()
    so.connect(node1)
    # print(c)

