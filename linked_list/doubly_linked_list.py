class DoubleNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, arr):
        """
        Given a list of elements it creates doubly linked list
        :param arr: List of elements
        :return: None
        """
        self.head = DoubleNode(arr[0])
        last = self.head
        for i in range(1, len(arr)):
            temp = DoubleNode(arr[i])
            temp.next = last.next
            temp.prev = last
            last.next = temp
            last = temp

    def length(self):
        """
        Calculates the length of doubly linked list
        :return: length of doubly linked list
        """
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
        return count

    def insert(self, pos, val):
        """
        Given value and its position function inserts element at
        that position in the linked list
        :param pos: position of the value
        :param val: value which should be inserted
        :return: None
        """
        if pos < 0 or pos > self.length():
            return
        temp_node = DoubleNode(val)
        p = self.head
        if pos == 0:
            temp_node.next = self.head
            self.head.prev = temp_node
            self.head = temp_node
        else:
            for i in range(pos - 1):
                p = p.next
            temp_node.next = p.next
            temp_node.prev = p
            if p.next:
                p.next.prev = temp_node
            p.next = temp_node

    def delete_node(self, pos):
        """
        Given a position of the node function deletes that
        particular if its in the range of linked list
        :param pos: position of node
        :return: value deleted
        """
        if pos < 1 or pos > self.length():
            return -1

        p = self.head
        if pos == 1 and self.head:
            self.head = self.head.next
            x = p.data
            del p
            if self.head:
                self.head.prev = None
        else:
            for i in range(pos - 1):
                p = p.next
            p.prev.next = p.next
            if p.next:
                p.next.prev = p.prev
            x = p.data
            del p
        return x

    def display(self):
        """
        Prints Doubly Linked List
        :return: None
        """
        p = self.head
        while p:
            print(p.data, end=' ')
            p = p.next
        print()

    def reverse(self):
        """
        this method reverses the doubly linked list
        :return: None
        """
        p = self.head
        temp = None
        while p is not None:
            temp = p.prev
            p.prev = p.next
            p.next = temp
            p = p.prev
        if temp is not None:
            self.head = temp.prev


def main():
    arr = [3, 2, 5, 1, 6, 10, 11]
    dl = DoublyLinkedList()
    dl.create(arr)
    print("Length of the linked list", dl.length())
    dl.display()
    dl.insert(3, 27)
    print("After inserting new element in the linked list")
    dl.display()
    dl.insert(0, 29)  # inserting at starting of the linked list
    dl.display()
    dl.insert(9, 30)  # inserting at last of the linked list
    dl.display()
    dl.delete_node(1)  # delete first element of the linked list
    dl.display()
    dl.delete_node(9)  # delete the last element of the linked list
    dl.display()
    dl.reverse()
    print("Reverse of doubly linked list is:", end=' ')
    dl.display()


if __name__ == '__main__':
    main()
