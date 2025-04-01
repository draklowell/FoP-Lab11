class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.head)

    def push(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def peek(self):
        if not self.head:
            raise ValueError("Stack is empty")

        return self.head.data

    def pop(self):
        data = self.peek()
        self.head = self.head.next
        self.size -= 1
        return data


class MyQueue:
    def __init__(self):
        self.forward = Stack()
        self.reversed = Stack()

    def _to_reversed(self):
        if self.reversed:
            return

        while self.forward:
            self.reversed.push(self.forward.pop())

    def _to_forward(self):
        if self.forward:
            return

        while self.reversed:
            self.forward.push(self.reversed.pop())

    def push(self, x: int) -> None:
        self._to_reversed()

        self.reversed.push(x)

    def pop(self) -> int:
        self._to_forward()

        return self.forward.pop()

    def peek(self) -> int:
        self._to_forward()

        return self.forward.peek()

    def empty(self) -> bool:
        return not self.forward and not self.reversed


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
