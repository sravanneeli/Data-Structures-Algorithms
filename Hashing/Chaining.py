from linked_list.linked_list_class import LinkedList


def hash_function(key):
    return key % 10


def insert(hash_table, key):
    index = hash_function(key)
    hash_table[index].insert_in_sorted_ll(key)


def main():
    hash_table = [LinkedList() for _ in range(10)]

    insert(hash_table, 12)  # at index 2
    insert(hash_table, 22)  # at index 2 it is matched by has function
    insert(hash_table, 42)
    hash_table[2].display()  # display all the elements that are stored at index 2 in form of chaining
    temp = hash_table[2].search(22)
    if temp:
        print("Data found")
    else:
        print("Not found")


if __name__ == '__main__':
    main()
