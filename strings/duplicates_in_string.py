# Using Bitwise operator
def find_duplicates_bit(a):
    h = 0; x = 0
    duplicates = []

    for i in range(len(a)):
        x = 1
        x = x << (ord(a[i]) - 97)
        if (x & h) > 0 :
            duplicates.append(a[i])
        else:
            h = h | x

    return duplicates
    





# Using Hashing
def find_duplicates(a):
    hash_arr = [0] * 26
    duplicates = []
    for i in range(len(a)):
        hash_arr[ord(a[i]) - 97] += 1
    for i in range(26):
        if hash_arr[i] > 1:
            duplicates.append(chr(i + 97))
    return duplicates


def main():
    a = 'finding'
    print(find_duplicates(a))
    print(find_duplicates_bit(a))

if __name__ == "__main__":
    main()