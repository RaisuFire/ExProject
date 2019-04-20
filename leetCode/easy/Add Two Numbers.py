# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans = ListNode(None)
        l = ans
        while l1 is not None or l2 is not None or carry:
            v1 = v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            l.next = ListNode(val)
            l = l.next
        return ans.next


        # ans = ListNode(None)
        # l = ans
        # m = 0
        # while l1 is not None and l2 is not None and m == 0:
        #     if l1 is None:
        #         l.next = l2
        #     if l2 is None:
        #         l.next = l1
        #     else:
        #         n = l1.val + l2.val
        #         if n < 10:
        #             if m > 0:
        #                 l.next = ListNode(l1.val + l2.val + 1)
        #             else:
        #                 l.next = ListNode(l1.val + l2.val)
        #             m = 0
        #         else:
        #             if m > 0:
        #                 l.next = ListNode(n - 10 + 1)
        #             else:
        #                 l.next = ListNode(n - 10)
        #             m = 1
        #     l1 = l1.next
        #     l2 = l2.next
        #     l = l.next
        # return ans.next.next.val

if __name__ == "__main__":
    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2 = ListNode(5, ListNode(6, ListNode(4)))
    l1 = ListNode(5)
    l2 = ListNode(5)
    so = Solution()
    c = so.addTwoNumbers(l1, l2)
    print(c)
