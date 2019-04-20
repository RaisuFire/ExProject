# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


if __name__ == "__main__":
    head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    node = ListNode(1)
    so = Solution()
    c = so.deleteNode()
    print(c)
