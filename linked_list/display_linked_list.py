from linked_list.linked_list_class import LinkedList, Node


# Create Linked list from given array
def create_ll(arr):
    ll = LinkedList()
    ll.head = Node(arr[0])
    temp = ll.head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return ll


# Display Linked List Elements using loop
def display_ll(p):
    while p:
        print(p.data, end=' ')
        p = p.next
    print()


# Display Linked List Recursively
def display_rec(p):
    if p:
        print(p.data, end=' ')
        display_rec(p.next)


# Reverse display of linked list
def display_rev(p):
    if p:
        display_rec(p.next)
        print(p.data, end=' ')


def main():
    arr = [3, 5, 7, 10, 15]
    ll = create_ll(arr)
    display_ll(ll.head)
    display_rec(ll.head)
    print()
    display_rev(ll.head)
    print()


if __name__ == "__main__":
    main()
