from collections import defaultdict
from queue import PriorityQueue


class FreqStack:
    def __init__(self):
        self.frequencies = defaultdict(int)
        self.queue = PriorityQueue()
        self.counter = 0

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.queue.put((-self.frequencies[val], self.counter, val))
        self.counter -= 1

    def pop(self) -> int:
        *_, val = self.queue.get()
        self.frequencies[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
