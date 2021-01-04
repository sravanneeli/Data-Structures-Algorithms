class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp

    def count(self):
        c = 0
        p = self.head
        while p:
            c += 1
            p = p.next
        return c

    def insert(self, pos, x):
        p = self.head
        if pos < 0 or pos > self.count():
            return
        t = Node(x)
        if pos == 0:
            t.next = self.head
            self.head = t
        else:
            for i in range(pos - 1):
                p = p.next
            t.next = p.next
            p.next = t

    def del_node(self, pos):
        """
        Delete a node in Linked List given the position of the Node.
        :param pos: index starts from 1
        :return: updated linked list with deleted node
        """
        q = None
        x = None
        p = self.head

        if pos < 1 or pos > self.count():
            return x

        if pos == 1:
            x = self.head.data
            self.head = self.head.next
            del p
        else:
            for i in range(pos - 1):
                q = p
                p = p.next

            if p:
                q.next = p.next
                x = p.data
                del p
        return x

    def display(self):
        p = self.head
        while p:
            print(p.data, end=' ')
            p = p.next
        print()
