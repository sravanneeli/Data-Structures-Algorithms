"""
There are three different methods to find the middle node of linked list
    1. finding the length of the linked list and traverse linked list till middle
    2. Using two pointer
    3. Using stack
"""
from linked_list.display_linked_list import create_ll
import math


# Using two pointers
def mid_point(ll):
    p = q = ll.head
    if ll.head:
        while q and q.next:
            q = q.next.next
            p = p.next
        print(p.data)


# Using length of the linked list
def mid_point_len(ll):
    p = ll.head
    mid = ll.count() // 2
    for i in range(mid):
        p = p.next
    print(p.data)


def mid_point_stack(ll):
    p = ll.head
    st = []
    while p:
        st.append(p.data)
        p = p.next
    for i in range(len(st) // 2 - 1):
        st.pop()
        
    return st[-1]


def main():
    A = [6, 3, 9, 10, 4, 2, 12, 24]
    ll = create_ll(A)
    ll.display()
    mid_point_len(ll)
    mid_point(ll)
    mid_point_stack(ll)


if __name__ == '__main__':
    main()
