from linked_list.linked_list_class import Node


class Queue:
    def __init__(self, size=0):
        self.size = size
        self.front = -1
        self.rear = -1
        self.__arr = [None] * size  # private attribute only belongs to class

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            self.rear += 1
            self.__arr[self.rear] = x

    def dequeue(self):
        if self.rear == self.front:
            print("Queue is Empty")
            return -1
        else:
            self.front += 1
            x = self.__arr[self.front]
            self.__arr[self.front] = None
            return x

    def display(self):
        for i in range(self.front + 1, self.rear + 1):
            print(self.__arr[i], end=' ')
        print()


class CircularQueue:
    def __init__(self, size=0):
        self.size = size
        self.front = 0
        self.rear = 0
        self.__arr = [None] * size  # private attribute only belongs to class

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        else:
            self.rear = (self.rear + 1) % self.size
            self.__arr[self.rear] = x

    def dequeue(self):
        if self.rear == self.front:
            print("Queue is Empty")
            return -1
        else:
            self.front = (self.front + 1) % self.size
            return self.__arr[self.front]

    def display(self):
        i = self.front + 1
        while i != (self.rear + 1) % self.size:
            print(self.__arr[i], end=' ')
            i = (i + 1) % self.size
        print(' ')


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)
        if new_node is None:
            print("Queue is Full")
        else:
            if self.front is None:
                self.front = self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            x = temp.data
            del temp
            return x

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def is_empty(self):
        return self.front is None


def queue_main():
    print("Queue using Array or List")
    q = Queue(int(input("Enter size of the queue: ")))
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(8)
    q.display()  # display the enqueued queue
    q.dequeue()  # dequeue from the queue
    q.display()


def circular_main():
    print("Queue is circular array or list")
    q = CircularQueue(int(input("Enter size of the circular queue: ")))
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(8)
    print(q.rear)
    q.dequeue()
    q.dequeue()
    q.enqueue(10)
    q.display()


def ll_queue():
    print("Queue using Linked List")
    q = LinkedListQueue()
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(10)
    q.display()
    q.dequeue()
    q.display()


if __name__ == '__main__':
    queue_main()
    circular_main()
    ll_queue()
