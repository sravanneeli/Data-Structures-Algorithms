from linked_list.linked_list_class import Node


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, arr):
        """
        Given a list of elements function creates Circular
        Linked List.
        :param arr: List of elements
        :return: None
        """
        self.head = Node(arr[0])
        self.head.next = self.head
        last = self.head

        for i in range(1, len(arr)):
            temp = Node(arr[i])
            temp.next = last.next
            last.next = temp
            last = temp

    def insert_at_pos(self, pos, val):
        """
        Updates the linked list with new inserted value at a given position
        :param pos: position of the value to be inserted
        :param val: value to be inserted
        :return: None
        """
        p = self.head
        new_node = Node(val)
        if pos == 0:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                while p.next != self.head:
                    p = p.next
                p.next = new_node
                new_node.next = self.head
                self.head = new_node
        else:
            for i in range(pos - 1):
                p = p.next
            new_node.next = p.next
            p.next = new_node

    def delete_node(self, pos):
        """
        function returns deleted element from the linked list
        :param pos: position of the element to be deleted
        :return: deleted element
        """
        p = self.head
        if pos == 1:
            while p.next is not self.head:
                p = p.next
            if p is self.head:
                del self.head
                self.head = None
            else:
                p.next = self.head.next
                x = self.head.data
                del self.head
                self.head = p.next
                return x
        else:
            for i in range(pos - 2):
                p = p.next
            q = p.next
            p.next = q.next
            x = q.data
            del q
            return x

    def display(self):
        """
        Prints the Linked List
        :return: None
        """
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=' '),
                temp = temp.next
                if temp == self.head:
                    break
            print()


def main():
    A = [3, 4, 5, 7, 1, 2, 9]
    cl = CircularLinkedList()
    cl.create(A)
    cl.display()
    cl.insert_at_pos(0, 54)  # insert 54 value at 0 th position
    cl.insert_at_pos(2, 24)  # insert at any other position
    cl.display()
    ele_del = cl.delete_node(4)  # delete any element except first
    print("Deleted Element is {}".format(ele_del))
    cl.display()
    ele_del_first = cl.delete_node(1)  # deleting first element
    print("Deleted First Element is {}".format(ele_del_first))
    cl.display()


if __name__ == '__main__':
    main()
