import math


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.set_arr = [-1] * vertices

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def union(self, u, v):
        if self.set_arr[u] < self.set_arr[v]:
            self.set_arr[u] += self.set_arr[v]
            self.set_arr[v] = u
        else:
            self.set_arr[v] += self.set_arr[u]
            self.set_arr[u] = v

    def find(self, u):
        x = u
        while self.set_arr[x] > 0:
            x = self.set_arr[x]

        while u != x:
            v = self.set_arr[u]
            self.set_arr[u] = x
            u = v

        return x

    def kruskals_algorithm(self):
        mst = []
        i = 0
        u = v = k = None
        included = [False] * len(self.graph)
        while i < self.V - 1:
            min_val = math.inf
            for j in range(0, len(self.graph)):
                if self.graph[j][2] < min_val and not included[j]:
                    min_val = self.graph[j][2]
                    u = self.graph[j][0]
                    v = self.graph[j][1]
                    k = j
            # find if cycle exists
            x = self.find(u)
            y = self.find(v)
            if x != y:
                mst.append([u, v, min_val])
                self.union(x, y)
                i += 1
            included[k] = True

        return mst


def main():
    g = Graph(7)
    g.addEdge(0, 1, 25)
    g.addEdge(0, 5, 5)
    g.addEdge(1, 2, 12)
    g.addEdge(1, 6, 10)
    g.addEdge(2, 3, 8)
    g.addEdge(3, 4, 16)
    g.addEdge(3, 6, 14)
    g.addEdge(4, 5, 20)
    g.addEdge(4, 6, 18)
    mst = g.kruskals_algorithm()
    for u, v, w in mst:
        print(f"{u:{5}} {v:{5}} {w:>{5}}")
    print(f"Min Spanning Tree Cost : {sum([k[2] for k in mst])}")


if __name__ == '__main__':
    main()
