import sys


def compute_sum(input_list):
    """input_list is a list of tuples (weight, length)"""
    res = 0
    total_len = 0
    for (w, l) in input_list:
        total_len += l
        res += w * total_len
    return res
    

def main(input_file):
    res = []
    with open(input_file) as inf:
        for k, line in enumerate(inf):
            if k == 0:
                n = int(k)
                continue
            res.append(tuple(int(_) for _ in line.split()))


    # sort by difference in DECREASING order, if it's a tie, break the tie by comparing weights
    res.sort(key=lambda x: (x[1] - x[0], -x[0]))

    print(list(map(lambda x: (x[1] - x[0], -x[0]), res)))

    print(res)
    return compute_sum(res)


if __name__ == "__main__":
    assert main('testcase1.txt') == 31814
    assert main('testcase2.txt') == 61545
    assert main('testcase3.txt') == 688647
