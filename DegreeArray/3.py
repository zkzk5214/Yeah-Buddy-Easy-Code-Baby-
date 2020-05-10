from collections import defaultdict


class Graph:
    """
    # defaultdict(<class 'list'>, {1: [2], 2: [], 3: [1, 2], 4: [3, 2]})
    """
    def __init__(self, directed=False):
        self.graph = defaultdict(list)  # Create a new dictionary-like object
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)  # {Key=frm:Value=list[to]}
        if self.directed is False:  # undirected or directed
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]
        return self.graph


if __name__ == '__main__':
    g = Graph(directed=False)
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            V1, V2 = list(map(int, i.split()))
            s = g.addEdge(V1, V2)

        for i in sorted(s.keys()):
            print(len(s[i]), end=" ")
