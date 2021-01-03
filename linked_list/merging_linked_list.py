"""
    Two Cases:
        1. Concatenating two Linked Lists
        2. Merging two sorted Linked Lists
"""

from linked_list.display_linked_list import create_ll, display_ll


# Concatenation
def concat(ll1, ll2):
    p = ll1.head
    while p.next:
        p = p.next
    p.next = ll2.head  # point the first list end to second list first
    ll2.head = None  # Detach the head of second list


# Merging Two sorted Linked List
def merge(ll1, ll2):
    p = ll1.head
    q = ll2.head
    if p.data < q.data:
        third = ll1
        last = p
        p = p.next
        last.next = None
    else:
        third = ll2
        last = q
        q = q.next
        last.next = None

    while p and q:
        if p.data < q.data:
            last.next = p
            last = p
            p = p.next
            last.next = None
        else:
            last.next = q
            last = q
            q = q.next
            last.next = None
    if p:
        last.next = p
    if q:
        last.next = q

    return third


# from this function we call merge linked list function
def merge_func(a, b):
    ll1 = create_ll(a)
    ll2 = create_ll(b)
    ll3 = merge(ll1, ll2)
    print("Merged Linked List: ", end=' ')
    display_ll(ll3.head)


def main():
    A = [10, 20, 30, 40, 50]
    B = [5, 15, 25, 35, 45]
    ll1 = create_ll(A)
    ll2 = create_ll(B)
    concat(ll1, ll2)
    print("Concatenated Linked List: ", end=' ')
    display_ll(ll1.head)
    merge_func(A, B)


if __name__ == '__main__':
    main()
