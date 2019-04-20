# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        newList = dummy
        while (l1 and l2):
            if l1.val <= l2.val:
                newList.next = l1
                l1 = l1.next
                newList = newList.next

            else:
                newList.next = l2
                l2 = l2.next
                newList = newList.next

        if l1:
            newList.next = l1
        elif l2:
            newList.next = l2

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(3)
    l2.next = ListNode(5)
    # l2.next.next = ListNode(4)
    so = Solution()
    c = so.mergeTwoLists(l1, l2)
    print(c)
