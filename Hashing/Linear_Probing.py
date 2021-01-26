SIZE = 10


def hash_function(key):
    return key % 10


def probe(hash_table, key):
    index = hash_function(key)
    i = 0
    while hash_table[(index + i) % SIZE]:
        i += 1
    return (index + i) % SIZE


def insert(hash_table, key):
    index = hash_function(key)
    if hash_table[index] is not None:
        index = probe(hash_table, key)
    hash_table[index] = key


def search(hash_table, key):
    index = hash_function(key)
    i = 0
    while hash_table[(index + i) % SIZE] != key and hash_table[(index + i) % SIZE] is not None:
        i += 1

    return hash_table[(index + i) % SIZE]


def main():
    hash_table = [None] * SIZE
    insert(hash_table, 12)
    insert(hash_table, 25)
    insert(hash_table, 35)
    insert(hash_table, 26)
    insert(hash_table, 36)
    print(hash_table)

    print("Key found" if search(hash_table, 37) else "Not found")


if __name__ == '__main__':
    main()
