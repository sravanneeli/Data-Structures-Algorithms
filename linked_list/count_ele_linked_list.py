from linked_list import LinkedList
from display_linked_list import create_ll

# Count number of elements using loop apporoach
def count_ll(p):
    c = 0
    while p:
        c += 1
        p = p.next
    return c

# Count number of elements using recursive apporoach
def count_rec(p):
    if p:
        return count_rec(p.next) + 1
    else:
        return 0

def main():
    A = [3, 5, 7, 10, 15]
    ll = LinkedList()
    ll = create_ll(A)
    count = count_ll(ll.head)
    print("Number of elements in Linked list : {}".format(count))
    print("Number of elements in Linked list : {}".format(count_rec(ll.head)))

if __name__ == "__main__":
    main()

