from linked_list import LinkedList, Node

# Create Linked list from given array
def create_ll(A):
    ll = LinkedList()
    ll.head = Node(A[0])
    temp = ll.head
    for i in range(1, len(A)):
        temp.next = Node(A[i])
        temp = temp.next

    return ll 

# Display Linked List Elements using loop
def display_ll(p):
    while p:
        print(p.data, end = ' ')
        p = p.next
    print()

# Display Linked List Reursively
def disp_rec(p):
    if p:
        print(p.data, end = ' ')
        disp_rec(p.next)

# Reverse display of linked list
def disp_rev(p):
    if p:
        disp_rec(p.next)
        print(p.data, end = ' ')
    

def main():
    A = [3, 5, 7, 10, 15]
    ll = create_ll(A)
    display_ll(ll.head)
    disp_rec(ll.head)
    print()
    disp_rev(ll.head)
    print()
    

if __name__ == "__main__":
    main()