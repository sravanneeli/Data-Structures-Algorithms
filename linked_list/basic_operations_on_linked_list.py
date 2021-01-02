from linked_list.display_linked_list import create_ll
import math

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

# Sum of elements of linked list
def sum_ll(p):
    if p:
        return sum_ll(p.next) + p.data
    else:
        return 0

def max_ll(p):
    if p:
        x = max_ll(p.next)
        return x if x > p.data else p.data
    else:
        return -math.inf
        
def main():
    A = [3, 5, 7, 10, 15]
    ll = create_ll(A)
    count = count_ll(ll.head)
    print("Number of elements in Linked list : {}".format(count))
    print("Number of elements in Linked list : {}".format(count_rec(ll.head)))
    print("Sum of all elements in the Linked List: {}".format(sum_ll(ll.head)))
    print("Max of all elements in the Linked List: {}".format(max_ll(ll.head)))

if __name__ == "__main__":
    main()
