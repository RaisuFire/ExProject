# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        first = head
        cur = head.next
        while cur is not None:
            head.next = cur.next
            cur.next = first
            first = cur
            cur = head.next
        return first

    # def reverseList(self, head):
    #     return self._reverse(head)
    #
    # def _reverse(self, node, prev=None):
    #     if not node:
    #         return prev
    #     n = node.next
    #     node.next = prev
    #     return self._reverse(n, node)


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    so = Solution()
    c = so.reverseList(node1)
    # print(c)

