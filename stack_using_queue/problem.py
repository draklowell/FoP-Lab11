class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.head)

    def push(self, data):
        if not self.head:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next

        self.size += 1

    def peek(self):
        if not self.head:
            raise ValueError("Queue is empty")

        return self.head.data

    def pop(self):
        data = self.peek()
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1
        return data


class MyStack:
    def __init__(self):
        self.queue = Queue()
        self.position = 0

    def _shift(self):
        if not self.queue:
            return

        self.queue.push(self.queue.pop())
        self.position += 1
        self.position %= len(self.queue)

    def _shift_back(self):
        while self.position != 0:
            self._shift()

    def _shift_forward(self):
        while self.position != len(self.queue) - 1:
            self._shift()

    def push(self, x: int) -> None:
        self._shift_back()
        self.queue.push(x)

    def pop(self) -> int:
        self._shift_forward()
        return self.queue.pop()

    def top(self) -> int:
        self._shift_forward()
        return self.queue.peek()

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
