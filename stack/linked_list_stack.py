from linked_list.linked_list_class import Node


def is_full():
    new_node = Node()
    if new_node is None:
        return True
    return False


class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        if new_node is None:
            print("Stack Overflow")
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        x = -1
        if self.top is None:
            print("Stack Underflow")
        else:
            p = self.top
            self.top = self.top.next
            x = p.data
            del p
        return x

    def is_empty(self):
        return self.top is None

    def peek(self, pos):
        p = self.top
        i = 0
        while i < (pos - 1) and p:
            p = p.next
        if p:
            return p.data
        else:
            return -1

    def st_top(self):
        if self.top:
            return self.top.data
        return -1

    def display(self):
        p = self.top
        while p:
            print(p.data, end=' ')
            p = p.next
        print()


def main():
    st = LinkedListStack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.display()
    print(st.st_top())


if __name__ == '__main__':
    main()
