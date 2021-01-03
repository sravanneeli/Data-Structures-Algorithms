"""
    Remove Duplicates from a sorted linked list
"""

from linked_list.display_linked_list import create_ll, display_ll


def remove_dup(p):
    q = p.next

    while q:
        if q.data != p.data:
            p = q
            q = q.next
        else:
            p.next = q.next
            del q
            q = p.next


def main():
    A = [3, 5, 5, 8, 8, 8, 9]
    ll = create_ll(A)
    remove_dup(ll.head)
    print("Linked List after removing duplicates : {}".format(display_ll(ll.head)))


if __name__ == '__main__':
    main()
