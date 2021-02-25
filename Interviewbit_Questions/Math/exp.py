for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    new = []
    output = [0] * n
    for i in range(n):
        new.append([i, arr[i]])
    for i in range(1, n):
        x = new[i]
        j = i - 1
        while j > -1 and new[j][1] < x[1]:
            new[j + 1] = new[j]
            j -= 1
        new[j + 1] = x

    for i in range(n):
        output[new[i][0]] = i + 1

    print(*output)