# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []

        o_head = ListNode(None)
        o_head.next = head
        head = o_head

        while o_head and o_head.next:
            if o_head.next.val == val:
                o_head.next = o_head.next.next
            else:
                o_head = o_head.next

        return head.next


    def llistprint(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next


if __name__ == "__main__":
    node = ListNode(1)
    # node1 = ListNode(2)
    # node2 = ListNode(6)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    # node6 = ListNode(6)
    # node.next = node1
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    so = Solution()
    so.removeElements(node, 1)
    so.llistprint(node)
