# class MyQueue(object):
#
#     def __init__(self, ):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = []
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.queue.append(x)
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         x = self.queue.pop(0)
#         return x
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         return self.queue[0]
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return len(self.queue) == 0

class MyStack(object):
    def __init__(self, ):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def peek(self):
        self.stack[0]

    def empty(self):
        return len(self.stack) == 0


class MyQueue(object):
    def __init__(self, stack1, backup):
        self.stack = stack1
        self.backup = backup

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.push(x)

    def pop(self):
        if self.backup.empty():
            while self.stack.empty is False:
                self.backup.push(self.stack.pop)
        return self.backup.pop()

    def peek(self):
        if self.backup.empty():
            while self.stack.empty is False:
                self.backup.push(self.stack.pop)
        return self.backup.peek()

    def empty(self):
        return self.stack.empty() and self.backup.empty


if __name__ == "__main__":
    queue = MyQueue();
    queue.push(1)
    queue.push(2)
    # print(queue.queue)
    queue.peek()
    print(queue.queue)
    queue.pop()
    # print(queue.pop())
    print(queue.queue)
    queue.empty()
    print(queue.empty())
