def min_lights(A, b):
    n = len(A)
    if b == 0:
        return -1
    i = 0
    bulbs = 0
    while i < n:
        pos = -1
        for j in range(max(0, i - b + 1), min(i + b, n)):
            if A[j] == 1:
                pos = j

        if pos == -1:
            return -1
        bulbs += 1
        i = pos + b

    return bulbs


def main():
    A = [0, 0, 1, 1, 0, 0, 0, 1]
    b = 3

    print(f"Min bulbs required to cover the floor: {min_lights(A, b)}")


if __name__ == '__main__':
    main()
