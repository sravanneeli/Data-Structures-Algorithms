"""
    Stack using fixed size of array.
    By default python lists supports stack operations like and peek operations.
"""


class Stack:
    def __init__(self, size=0):
        self.size = size
        self.top = -1
        self.arr = []

    def create(self):
        """
        Create Empty Stack with predefined size provided by
        the user
        :return: None
        """
        if self.size == 0:
            self.size = int(input("Enter size of the stack to be created: "))
        self.arr = [None] * self.size

    def display(self):
        """
        Display Stack elements
        :return: None
        """
        for i in range(self.top, -1, -1):
            print(self.arr[i], end=' ')
        print()

    def push(self, x):
        """
        Push the element at the top of the stack
        :param x: value to pushed
        :return: None
        """
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = x

    def pop(self):
        """
        pop the top element of the stack
        :return: element popped
        """
        x = -1
        if self.top == -1:
            print("Stack is Underflow")
        else:
            x = self.arr[self.top]
            self.top -= 1
        return x

    def peek(self, index):
        """
        Peek the element at the given index
        :param index: index value
        :return: value at the that index value
        """
        x = -1
        if (self.top - index + 1) < 0:
            print("Invalid Index")
        else:
            x = self.arr[self.top - index + 1]
        return x

    def is_empty(self):
        """
        Check whether stack is empty
        :return: None
        """
        return self.top == -1

    def is_full(self):
        """
        Check whether stack is full
        :return: None
        """
        return self.top == self.size - 1

    def top_ele(self):
        """
        Get the top of element of the stack
        :return: top element of the stack
        """
        if not self.is_empty():
            return self.arr[self.top]
        return -1


def main():
    st = Stack()
    st.create()

    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)

    # print(st.pop())
    # print(st.pop())
    # print(st.pop())
    print(st.peek(2))
    st.display()


if __name__ == '__main__':
    main()
