"""
    Finding the point of intersection of two linked lists
"""

from linked_list.display_linked_list import create_ll


def intersection(ll1, ll2):
    p = ll1.head
    q = ll2.head
    stack1 = []
    stack2 = []

    while p:
        stack1.append(p)
        p = p.next
    while q:
        stack2.append(q)
        q = q.next
    last = None
    while stack1[-1] == stack2[-1]:
        last = stack1[-1]
        stack1.pop()
        stack2.pop()
    return last.data


def main():
    A = [8, 6, 3, 9, 10, 4, 2, 12]
    B = [20, 30, 40]
    ll1 = create_ll(A)
    ll2 = create_ll(B)
    ll2.head.next.next.next = ll1.head.next.next.next  # forming a intersection point
    ll1.display()
    ll2.display()
    print("Intersection of above two linked lists is: {}".format(intersection(ll1, ll2)))


if __name__ == '__main__':
    main()
