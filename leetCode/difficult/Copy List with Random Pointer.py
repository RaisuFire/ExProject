# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        copy = {}
        cur = head
        while cur:
            if cur not in copy:
                copy[cur] = RandomListNode(cur.label)
            if cur.next:
                if cur.next not in copy:
                    copy[cur.next] = RandomListNode(cur.next.label)
                copy[cur].next = copy[cur.next]
            if cur.random:
                if cur.random not in copy:
                    copy[cur.random] = RandomListNode(cur.random.label)
                copy[cur].random = copy[cur.random]
            cur = cur.next
        return copy[head]


if __name__ == '__main__':
    ...