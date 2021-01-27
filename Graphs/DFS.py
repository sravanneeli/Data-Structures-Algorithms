def dfs(adj, start, visited):
    if not visited[start]:
        print(start)
        visited[start] = True
        for v in range(len(adj[0])):
            if adj[start][v]:
                dfs(adj, v, visited)


def main():
    adj = [[0, 1, 1, 0, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [0, 1, 1, 0, 1, 1],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0, 0]]
    visited = [False] * len(adj)
    dfs(adj, 0, visited)


if __name__ == '__main__':
    main()
