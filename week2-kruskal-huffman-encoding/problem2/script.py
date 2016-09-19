import itertools
import copy
import unittest


def read(input_file):
    nodes = []

    with open(input_file) as inf:
        for k, line in enumerate(inf):
            if k == 0:
                num_nodes, num_bits = [int(_) for _ in line.split()]
                continue

            node = tuple(int(_) for _ in line.split())
            nodes.append(node)

    return num_nodes, num_bits, nodes


def huffman_dist(n1, n2):
    d = 0
    for i, j in zip(n1, n2):
        if i != j:
            d += 1
    return d


def gen_neighbours(node):
    num_bits = 2


    # neighbours with no bit flipped
    node_copy = copy.copy(node)
    neighbours = [node_copy]

    # neighbours with two bits flipped
    for (i, j) in itertools.combinations(range(len(node)), num_bits):
        node_copy = list(copy.copy(node))
        node_copy[i] = 1 - node[i]
        node_copy[j] = 1 - node[j]
        neighbours.append(tuple(node_copy))

    # neighbours with only one bit flipped
    for i in range(len(node)):
        node_copy = list(copy.copy(node))
        node_copy[i] = 1 - node[i]
        neighbours.append(tuple(node_copy))

    return neighbours


class Node(object):
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank

    def __str__(self):
        return 'data: {0}, rank: {1}'.format(self.data, self.rank)

    def __repr__(self):
        return '{0}'.format(self)


def make_set(data, mapping):
    """mapping is used to store union find data"""
    n = Node(data)
    n.parent = n
    n.rank = 0
    mapping[data] = n


def find_set(node):
    if node.parent == node:
        return node
    else:
        return find_set(node.parent)


def union(data1, data2, mapping):
    n1 = mapping.get(data1)
    n2 = mapping.get(data2)

    p1 = find_set(n1)
    p2 = find_set(n2)

    # if they are part of same set do nothing
    if p1.data == p2.data:
        return False

    if p1.rank >= p2.rank:
        if p1.rank == p2.rank:
            p1.rank += 1
        p2.parent = p1
    else:
        p1.parent = p2
    return True


def main(input_file):
    num_nodes, num_bits, nodes = read(input_file)
    mapping = {}

    print('initializing sets for each vertex')
    for n in nodes:
        make_set(n, mapping)

    print('union neighbours')
    for k, n in enumerate(nodes):
        neighbours = gen_neighbours(n)
        for ne in neighbours:
            if ne in mapping:
                union(n, ne, mapping)
        if (k + 1) % 1000 == 0:
            print('{0} nodes have been processed'.format(k + 1))

    print('calculating number of clusters')
    clusters = set()
    for i in mapping.values():
        clusters.add(find_set(i))

    # return number of clusters
    return len(clusters)


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(main('testcase1.txt'), 7)
        self.assertEqual(main('testcase2.txt'), 4)


if __name__ == "__main__":
    print(main('clustering_big.txt'))
    # unittest.main()
