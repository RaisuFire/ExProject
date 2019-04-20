
# Definition for a Node.
from queue import Queue


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(Node(node))

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = [root]
        result = []
        while stack:
            temp = stack.pop()
            result.append(temp.val)
            for x in temp.children:
                stack.append(x)
            # [stack.append(x) for x in temp.children]
        # return result[::-1]


if __name__ == "__main__":
    node = Node(1)
    node1 = Node(3)
    node.add_child(node1)
    node.add_child(2)
    node.add_child(4)
    node1.add_child(5)
    node1.add_child(6)
    so = Solution()
    c = so.postorder(node)
    print(c)