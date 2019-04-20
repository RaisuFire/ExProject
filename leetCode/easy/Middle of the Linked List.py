# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        p = head
        c = 1
        while p.next is not None:
            c += 1
            p = p.next
        a = c // 2 + 1
        while a > 1:
            a -= 1
            head = head.next
        return head




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
    c = so.middleNode(node1)
    print(c.val)

