import unittest
import math
import sys
from collections import defaultdict



def generate_graph(input_file):
    # init a graph based on the input file
    graph = {}
    with open(input_file) as inf:
        for k, line in enumerate(inf):
            if k == 0:
                m, n = [int(_) for _ in line.split()]
                continue

            n1, n2, cost = [int(_) for _ in line.split()]

            if n1 not in graph:
                graph[n1] = [(n2, cost)]
            else:
                graph[n1].append((n2, cost))

            if n2 not in graph:
                graph[n2] = [(n1, cost)]
            else:
                graph[n2].append((n1, cost))
    return graph


def main(input_file):
    # https://youtu.be/z1L3rMzG1_A?t=4m27s
    graph = generate_graph(input_file)

    key_dict, parent = {}, {}

    for v in graph.keys():
        key_dict[v] = math.inf
        parent[v] = None

    v0 = list(graph.keys())[0]
    key_dict[v0] = 0

    A = []              # collection of edges forming the minimum spanning tree
    Q = set(graph.keys())

    while Q:
        u = min(Q, key=lambda x: key_dict[x])
        # print(Q, u)
        Q.discard(u)
        if parent[u] is not None:
            A.append((u, *parent[u]))
        for (v, weight) in graph[u]:
            if v in Q and weight < key_dict[v]:
                parent[v] = (u, weight)
                key_dict[v] = weight

    # print(A)
    
    # return the overall cost of a minimum spanning tree
    return (sum(_[2] for _ in A))


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(main('testcase1.txt'), -236)


if __name__ == "__main__":
    print(main('edges.txt'))
    unittest.main()
