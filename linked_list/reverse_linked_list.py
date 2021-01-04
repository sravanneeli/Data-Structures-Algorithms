"""
    There are three methods to reverse the linked list.
        1. Using auxiliary array
        2. Reverse Links using loop
        3. Reverse Links using recursive approach
"""
from linked_list.display_linked_list import create_ll, display_ll


# Reverse Links using recursive approach
def reverse_rec(p, ll, q=None):
    if p is not None:
        reverse_rec(p.next, ll, p)
        p.next = q
    else:
        ll.head = q


# Reversing Links Using Loop
def reverse(ll):
    p = ll.head
    q = None
    while p:
        r = q
        q = p
        p = p.next
        q.next = r
    ll.head = q


# Using auxiliary array
def reverse_aux(ll):
    p = ll.head
    aux = []  # auxiliary array
    while p:
        aux.append(p.data)
        p = p.next
    p = ll.head
    i = len(aux) - 1
    while p:
        p.data = aux[i]
        p = p.next
        i -= 1


def main():
    A = [3, 5, 6, 2, 12, 4, 10]
    ll = create_ll(A)
    reverse_aux(ll)
    print("Original Linked List: {}".format(A))
    print("Reversed Linked List using auxiliary array:", end=' ')
    ll.display()
    print("Reversed Linked List using Loop approach:", end=' ')
    reverse(ll)
    ll.display()
    print("Reversed Linked List using Recursive approach:", end=' ')
    reverse_rec(ll.head, ll)
    ll.display()


if __name__ == '__main__':
    main()
