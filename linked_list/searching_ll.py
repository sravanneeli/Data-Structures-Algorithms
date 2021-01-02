from linked_list.display_linked_list import create_ll


# Loop approach
def search(p, key):
    while p:
        if p.data == key:
            return p
        else:
            p = p.next


# Recursive approach
def search_rec(p, key):
    if p == None:
        return None
    if p.data == key:
        return p
    return search_rec(p.next, key)


def main():
    A = [3, 5, 7, 10, 15]
    ll = create_ll(A)

    temp = search(ll.head, 10)

    if temp:
        print("Key is found", temp.data)
    else:
        print("Key not found")

    tempR = search_rec(ll.head, 15)

    if tempR:
        print("Key is found", tempR.data)
    else:
        print("Key not found")


if __name__ == "__main__":
    main()
