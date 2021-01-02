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
    if p is None:
        return None
    if p.data == key:
        return p
    return search_rec(p.next, key)


def main():
    arr = [3, 5, 7, 10, 15]
    ll = create_ll(arr)

    temp = search(ll.head, 10)

    if temp:
        print("Key is found", temp.data)
    else:
        print("Key not found")

    tempr = search_rec(ll.head, 15)

    if tempr:
        print("Key is found", tempr.data)
    else:
        print("Key not found")


if __name__ == "__main__":
    main()
