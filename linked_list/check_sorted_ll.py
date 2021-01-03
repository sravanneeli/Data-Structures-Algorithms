"""
Check whether the linked list is sorted or not
"""
import math
from linked_list.display_linked_list import create_ll


def is_sorted(p):
    x = -math.inf
    while p:
        if p.data > x:
            x = p.data
            p = p.next
        else:
            return False
    return True


def main():
    A = [3, 5, 8, 12, 16]  # sorted
    B = [3, 5, 7, 2, 8]  # not sorted
    ll1 = create_ll(A)
    ll2 = create_ll(B)

    if is_sorted(ll1.head):
        print("Given Linked List is sorted")
    else:
        print("Linked List is not sorted")

    if is_sorted(ll2.head):
        print("Given Linked List is sorted")
    else:
        print("Linked List is not sorted")


if __name__ == '__main__':
    main()
