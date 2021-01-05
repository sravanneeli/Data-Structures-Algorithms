"""
Representation of polynomial using a linked list
"""


class PolyNode:
    def __init__(self, coefficient=None, exp=None):
        self.coefficient = coefficient
        self.exp = exp
        self.next = None


class PolyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        last = None
        num = int(input("Enter number of terms: "))
        print("Enter each term with coefficient and exponent")
        for i in range(num):
            coefficient, exp = map(int, input().split())
            new_node = PolyNode(coefficient, exp)
            if self.head is None:
                self.head = last = new_node
            else:
                last.next = new_node
                last = new_node

    def display(self):
        p = self.head
        while p:
            print("{}x^{}".format(p.coefficient, p.exp), end='+')
            p = p.next
        print()

    def eval(self, x):
        p = self.head
        val = 0
        while p:
            val += p.coefficient * pow(x, p.exp)
            p = p.next
        return val


def main():
    pl = PolyLinkedList()
    pl.create()
    pl.display()
    x = 4
    val = pl.eval(x)
    print("Evaluation of the given function {} is: {}".format(x, val))


if __name__ == '__main__':
    main()
