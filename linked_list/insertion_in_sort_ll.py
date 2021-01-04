from linked_list.insertion_in_ll import insert
from linked_list.linked_list_class import Node, LinkedList


# insertion a element in sorted linked list
def insert_in_sorted_ll(x, p, ll):
    q = None
    t = Node(x)
    if ll.head is None:
        ll.head = t
    else:
        while p and p.data < x:
            q = p
            p = p.next

        if p is ll.head:
            t.next = ll.head
            ll.head = t
        else:
            t.next = q.next
            q.next = t


def main():
    A = [3, 7, 9, 15, 20]
    ll = LinkedList()
    for i in range(len(A)):
        insert(ll.head, i, A[i], ll)
    insert_in_sorted_ll(8, ll.head, ll)  # insertion at middle
    insert_in_sorted_ll(1, ll.head, ll)  # insertion at starting
    insert_in_sorted_ll(25, ll.head, ll)  # insertion at ending
    ll.display()  # display linked list after inserting the element
    new_ll = LinkedList()
    insert_in_sorted_ll(55, new_ll.head, new_ll)  # inserting when no node is there
    insert_in_sorted_ll(50, new_ll.head, new_ll)  # insert new element for new element
    new_ll.display()


if __name__ == '__main__':
    main()
