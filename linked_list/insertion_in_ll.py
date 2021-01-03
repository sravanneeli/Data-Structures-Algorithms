from linked_list.display_linked_list import create_ll, display_ll
from linked_list.linked_list_class import Node, LinkedList
from linked_list.basic_operations_on_linked_list import count_ll


def insert(p, pos, x, ll):
    if pos < 0 or pos > count_ll(p):
        return
    t = Node(x)
    if pos == 0:
        t.next = ll.head
        ll.head = t
    else:
        for i in range(pos-1):
            p = p.next
        t.next = p.next
        p.next = t


def main():
    A = [4, 5, 12, 2, 1, 23, 5, 23]
    ll = create_ll(A)
    insert(ll.head, len(A), 26, ll)  # insert at end of the linked list
    display_ll(ll.head)
    insert(ll.head, 0, 9, ll)  # insert in position 0
    display_ll(ll.head)
    insert(ll.head, 4, 8, ll)  # insert in middle
    display_ll(ll.head)
    new_ll = LinkedList()
    insert(new_ll.head, 0, 8, new_ll)
    insert(new_ll.head, 1, 3, new_ll)
    insert(new_ll.head, 2, 6, new_ll)
    insert(new_ll.head, 0, 5, new_ll)
    insert(new_ll.head, 3, 9, new_ll)
    display_ll(new_ll.head)


if __name__ == "__main__":
    main()
