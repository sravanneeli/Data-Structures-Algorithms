def plusOne(A):
    n = len(A)
    new = []
    B = 1
    for _ in range(n):
        ele = A.pop()
        ele += B
        B = ele // 10
        new.append(ele % 10)
    if B == 1:
        new.append(1)
    new = new[::-1]
    while new[0] == 0:
        new.pop(0)
    return new


def main():
    A = [0, 0, 9, 9, 9]
    print(f"Added one to {A} gives {plusOne(A)}")


if __name__ == '__main__':
    main()
