from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)  # Create a new dictionary-like object
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)      # {Key:Value} = {frm:list[to]}
        # defaultdict(<class 'list'>, {1: [2], 2: [], 3: [1, 2], 4: [3, 2]})
        if self.directed is False:      # Undirected or Directed
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    # A recursive function used by TopologicalSort
    def topoSortvisit(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortvisit(i, visited, sortlist)
        sortlist.insert(0, s)
        # [2]           First insert the vertex that have no value(sink)
        # [1, 2]        then insert the vertex that all value are visited
        # [3, 1, 2]     and so on
        # [4, 3, 1, 2]

    def topoSort(self):
        visited = {i: False for i in self.graph}
        # {1: False, 2: False, 3: False, 4: False}
        sortlist = []

        for v in self.graph:
            if not visited[v]:
                self.topoSortvisit(v, visited, sortlist)

        print(' '.join(map(str, sortlist)))


if __name__ == '__main__':
    g = Graph(directed=True)
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            V1, V2 = list(map(int, i.split()))
            g.addEdge(V1, V2)
    g.topoSort()
