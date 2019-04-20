
# Definition for a Node.
from queue import Queue


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q = Queue()
        q.put(root)
        nums = []
        while not q.empty():
            n = q.get()
            if root is None:
                continue
            for i in root.children:
                q.put(i)
            nums.append(root.val)
        return nums


if __name__ == "__main__":
    node = Node(1)
    node.add_child(2)
    node.add_child(4)
    B = Node(3)
    node.add_child(B)
    B.add_child(5)
    B.add_child(6)
    so = Solution()
    c = so.levelOrder(node)
    print(c)
