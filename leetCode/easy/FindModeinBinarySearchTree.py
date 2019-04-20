# Definition for a binary tree node.



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def proc(data):
    data*2


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        mydir = {}
        res = []

        while queue:
            temq = []
            for node in queue:
                mydir[node.val] = mydir.get(node.val, 0) + 1
                if node.left:
                    temq.append(node.left)
                if node.right:
                    temq.append(node.right)
            queue = temq
        maxfreq = max(mydir.values())
        for key, val in mydir.items():
            if val == maxfreq:
                res.append(key)
        return res

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = None
    t.right = TreeNode(2)
    t.right.right = TreeNode(2)
    so = Solution()
    c = so.findMode(t)
    print(c)
