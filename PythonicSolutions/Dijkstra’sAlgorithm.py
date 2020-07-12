"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
h) Dijkstra’s Algorithm
"""
import sys


class Chart():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def imprint_solution(self, distance):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", distance[node])

    def min_distance(self, distance, sptSet):

        minimum = sys.maxsize

        for v in range(self.V):
            if distance[v] < minimum and sptSet[v] == False:
                minimum = distance[v]
                min_index = v

        return min_index

    def dijkstra_algorithm(self, src):

        distance = [sys.maxsize] * self.V
        distance[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.min_distance(distance, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]

        self.imprint_solution(distance)


g = Chart(10)
g.graph = [[0, 7, 0, 0, 3, 0, 0, 0, 0, 1],
           [5, 0, 0, 9, 0, 0, 0, 13, 0, 0],
           [0, 0, 0, 8, 0, 0, 5, 0, 2, 0],
           [0, 7, 0, 0, 0, 4, 0, 12, 0, 6],
           [8, 0, 0, 15, 0, 0, 2, 0, 0, 0],
           [0, 5, 4, 0, 0, 1, 0, 0, 0, 3],
           [0, 3, 0, 0, 2, 0, 0, 1, 6, 0],
           [7, 0, 0, 0, 3, 0, 0, 0, 6, 16],
           [1, 0, 0, 0, 2, 0, 0, 7, 0, 9],
           [0, 3, 0, 0, 5, 7, 0, 0, 0, 3]
           ]

g.dijkstra_algorithm(1)