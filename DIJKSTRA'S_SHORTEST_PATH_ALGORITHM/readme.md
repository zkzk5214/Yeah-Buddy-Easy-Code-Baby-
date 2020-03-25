Dijkstra's shortest path algorithm
Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node (a in our case) to all other nodes in the graph.

To keep track of the total cost from the start node to each destination we will make use of the distance instance variable in the Vertex class. The distance instance variable will contain the current total weight of the smallest weight path from the start to the vertex in question. The algorithm iterates once for every vertex in the graph; however, the order that we iterate over the vertices is controlled by a priority queue (actually, in the code, I used heapq).

The value that is used to determine the order of the objects in the priority queue is distance. When a vertex is first created distance is set to a very large number.

When the algorithm finishes the distances are set correctly as are the predecessor (previous in the code) links for each vertex in the graph.

https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
