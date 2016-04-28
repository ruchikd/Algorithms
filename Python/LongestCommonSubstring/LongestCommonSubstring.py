def longest_common_substring(s1, s2):
    if s1 is None or s2 is None:
        return

    # create a 2-dimensional array of size [len(s2)][len(s1)]
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0

    print m
    print x_longest
    print longest

    return s1[x_longest - longest: x_longest]

    '''
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]
    '''

def main():
    print longest_common_substring("bcbcdabcbd", "bcbcbcbca")

if __name__ == '__main__':
    main()