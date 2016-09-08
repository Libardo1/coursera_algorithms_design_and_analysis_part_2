import sys
import unittest


def compute_sum(input_list):
    """input_list is a list of tuples (weight, length)"""
    res = 0
    total_len = 0
    for (w, l) in input_list:
        total_len += l
        res += w * total_len
    return res
    

def main(input_file, key='diff'):
    res = []
    with open(input_file) as inf:
        for k, line in enumerate(inf):
            if k == 0:
                n = int(k)
                continue
            res.append(tuple(int(_) for _ in line.split()))

    if key == 'diff':
        # sort by difference in DECREASING order, if it's a tie, break the tie
        # by comparing weights
        res.sort(key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    elif key == 'ratio':
        # sort by ratio in DECREASING order, how to break a tie doesn't matter
        res.sort(key=lambda x: x[0] / x[1], reverse=True)

    print(list(map(lambda x: (x[1] - x[0], -x[0]), res)))

    print(res)
    return compute_sum(res)


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(main('testcase1.txt'), 31814)
        self.assertEqual(main('testcase1.txt', key='ratio'), 31814)
        self.assertEqual(main('testcase2.txt'), 61545)
        self.assertEqual(main('testcase2.txt', key='ratio'), 60213)
        self.assertEqual(main('testcase3.txt'), 688647)
        self.assertEqual(main('testcase3.txt', key='ratio'), 674634)

if __name__ == "__main__":
    unittest.main()
