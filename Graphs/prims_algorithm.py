import math

inf = math.inf


def prims(cost, near):
    n = len(cost)
    min_edge = math.inf
    u = v = k = 0
    t = [[math.inf] * (n - 1), [math.inf] * (n - 1)]
    for i in range(n):
        for j in range(i, n):
            if cost[i][j] < min_edge:
                min_edge = cost[i][j]
                u = i
                v = j
    t[0][0] = u
    t[1][0] = v
    near[u] = near[v] = -1
    for i in range(n):
        if near[i] != -1:
            if cost[i][u] < cost[i][v]:
                near[i] = u
            else:
                near[i] = v
    print(u, v, min_edge)
    for i in range(1, n-1):
        min_value = math.inf
        for j in range(n):
            if cost[j][near[j]] < min_value and near[j] != -1:
                k = j
                min_value = cost[j][near[j]]

        print(k, near[k], min_value)

        t[0][i] = k
        t[1][i] = near[k]
        near[k] = -1
        # print(near)
        for j in range(n):
            if near[j] != -1 and cost[j][k] < cost[j][near[j]]:
                near[j] = k

    # for i in range(n - 1):
    #     print(t[0][i], t[1][i])


def main():
    cost = [[math.inf, 2, math.inf, 6, math.inf],
            [2, math.inf, 3, 8, 5],
            [math.inf, 3, math.inf, math.inf, 7],
            [6, 8, math.inf, math.inf, 9],
            [math.inf, 5, 7, 9, math.inf]]

    near = [math.inf for _ in range(len(cost))]
    # print(near)
    prims(cost, near)


if __name__ == '__main__':
    main()
