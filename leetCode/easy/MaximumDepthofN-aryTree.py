"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Node(object):
    ''' Node object that contains
        a data field and list of children '''

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        ''' Adds a child and returns that child '''
        child = Node(data)
        self.children.append(child)
        return child

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        n = 1
        for child in root.children:
            n = max(n, 1 + self.maxDepth(child))
        return n

if __name__ == '__main__':
    node = Node(1)
    node.add_child(2)
    node.add_child(3)
    node.add_child(4)
    node.children[0].add_child(4)
    # print(node.children[0].children[0].data)
    so = Solution()
    d = so.maxDepth(node)
    print(d)