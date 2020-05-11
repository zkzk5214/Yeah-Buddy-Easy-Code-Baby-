"""
Given: A simple graph with vertices in the edge list format.
Return: An array where is the sum of the degrees of 's neighbors.
"""
File = '.txt'

try:
    with open(File) as f:
        '''
        Read data in file:
        1st line: Number of vertices   Number of edges
        Subsequent lines: Edge given by two vertices
        '''
        V, E = map(int, f.readline().rstrip().split())
        e = [map(int, line.rstrip().split()) for line in f]
        Res = []

        # Neighbors dict = {Key=Vertices: Value= lists of adjacent vertices}
        neighbors = {k: [] for k in range(1, V + 1)}
        for v1, v2 in e:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        # {1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [3, 2], 5: []}

        # Degree of a vertex is the number of edges that connect to it
        # BUT double degree of a vertex is the number of edges that are
        # connected to ADJACENT vertices
        degree = {k: 0 for k in neighbors.keys()}
        for v in neighbors:                     # Every key(vertex)
            for n in neighbors[v]:              # Every value(neighbor) in specific key
                degree[v] += len(neighbors[n])  # Add the num of neighbor's degree

        for k, v in sorted(degree.items()):     # Sort key, add to res
            Res.append(v)

    listToStr = ' '.join(map(str, Res))
    print(listToStr)

except IOError as e:
    print('Operation failed: %s' % e.strerror)
    # IOError.strerror: No such file or directory
