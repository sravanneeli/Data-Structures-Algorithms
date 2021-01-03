from linked_list.display_linked_list import display_ll
from linked_list.linked_list_class import Node


# Linked List with to maintain last pointer
class LinkedListLast:
    def __init__(self):
        self.head = None
        self.last = None


# insertion at last of linked list
def insert_at_last(x, ll):
    t = Node(x)
    if ll.head is None:
        ll.head = ll.last = t
    else:
        ll.last.next = t
        ll.last = t


def main():
    ll = LinkedListLast()
    insert_at_last(5, ll)
    insert_at_last(8, ll)
    insert_at_last(9, ll)
    display_ll(ll.head)


if __name__ == '__main__':
    main()
