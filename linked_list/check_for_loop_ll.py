"""
 Check whether a linked list has loop in it or not
"""
from linked_list.display_linked_list import create_ll


def is_loop(head):
    p = q = head
    while p and q and q.next:
        p = p.next
        q = q.next.next
        if p == q:
            return True
    else:
        return False


def main():
    A = [10, 20, 30, 40, 50]
    ll = create_ll(A)
    t1 = ll.head.next
    t2 = ll.head.next.next.next.next
    t2.next = t1
    print("Loop present or not in Linked List ? {}".format(is_loop(ll.head)))


if __name__ == '__main__':
    main()
