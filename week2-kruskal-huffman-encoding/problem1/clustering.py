import unittest


def read_edges(input_file):
    edges = []

    with open(input_file) as inf:
        for k, line in enumerate(inf):
            if k == 0:
                num_nodes = int(line)
                continue

            n1, n2, cost = [int(_) for _ in line.split()]
            edges.append((n1, n2, cost))


    edges.sort(key = lambda x: x[2])
    return num_nodes, edges


def main(input_file, num_clusters):
    num_nodes, edges = read_edges(input_file)
    
    clusters = [set([i]) for i in range(1, num_nodes + 1)]

    while len(clusters) > num_clusters:
        n1, n2, cost = edges.pop(0)

        c1, c2 = None, None
        for c in clusters:
            if n1 in c:
                c1 = c
            elif n2 in c:
                c2 = c

        # print(clusters, n1, n2, c1, c2, c1 == c2)

        if c1 is not None and c2 is not None:
            unioned = c1.union(c2)
            clusters.append(unioned)
            clusters.remove(c1)
            clusters.remove(c2)


    # calculate maximum spacing between clusters

    node2cluster = {}

    for k, c in enumerate(clusters):
        for i in c:
            # use k as cluster id
            node2cluster[i] = (k, c)

    clustered_graph = {}

    for (n1, n2, cost) in edges:
        c1 = node2cluster[n1]
        c2 = node2cluster[n2]

        if c1[0] == c2[0]:
            continue

        key = tuple(sorted([c1[0], c2[0]]))
        if key in clustered_graph:
            if clustered_graph[key] > cost:
                clustered_graph[key] = cost
        else:
            clustered_graph[key] = cost
    # print(clustered_graph)

    min_spacing = min(clustered_graph.values())
    return min_spacing


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(main('testcase1.txt', 3), 35)
        self.assertEqual(main('testcase1.txt', 4), 17)
        self.assertEqual(main('testcase1.txt', 5), 7)

        self.assertEqual(main('testcase2.txt', 4), 7)
        self.assertEqual(main('testcase3.txt', 4), 2)



if __name__ == "__main__":
    print(main('clustering1.txt', 4))
    unittest.main()
