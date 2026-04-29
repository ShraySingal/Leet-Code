class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = None
        self.back = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp = Node(value)
        if self.isEmpty():
            self.front = self.back = temp
        else:
            self.back.next = temp
            self.back = temp
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.front = self.back = None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
