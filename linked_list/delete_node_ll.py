"""
Two cases
    1. Delete first Node
    2. Delete a Node at a given position
"""
from linked_list.display_linked_list import create_ll, display_ll


def delete_node(pos, ll, p):
    q = None
    x = None
    if pos == 1:
        x = ll.head.data
        ll.head = ll.head.next
        del p
    else:
        for i in range(pos - 1):
            q = p
            p = p.next

        if p:
            q.next = p.next
            x = p.next
            del p
    return x


def main():
    A = [5, 3, 2, 12, 21, 5]
    ll = create_ll(A)
    delete_node(1, ll, ll.head)  # delete first Node
    delete_node(5, ll, ll.head)  # delete last Node
    display_ll(ll.head)


if __name__ == '__main__':
    main()
