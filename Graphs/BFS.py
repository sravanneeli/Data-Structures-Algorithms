from collections import deque


def bfs(adj, start):
    q = deque()
    visited = [False] * len(adj)
    print(start)
    visited[start] = True
    q.append(start)
    while q:
        u = q.popleft()
        for i in range(len(adj[0])):
            if adj[u][i] == 1 and visited[i] == 0:
                print(i)
                q.append(i)
                visited[i] = True


def main():
    adj = [[0, 1, 1, 1, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 1, 1],
           [1, 0, 1, 0, 1],
           [0, 0, 1, 1, 0]]
    bfs(adj, 2)


if __name__ == '__main__':
    main()
