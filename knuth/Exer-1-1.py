# solutions to problems in
# Art of Computer Programming - Knuth

__author__ = 'nagarajan'

def solve1(abcd):
    t = abcd[0]
    for idx1 in range(len(abcd)-1):
        abcd[idx1] = abcd[idx1 + 1]

    abcd[-1] = t
    return abcd

def solve4(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
    return gcd(a, b)

def solve6(n=5, nExp=1000):
    """
    The theoretical solution is 2.6
    """
    opCount = [0]
    def gcd(a, b):
        if b == 0:
            return a
        opCount[0] += 1
        return gcd(b, a%b)

    totalOps = 0
    for m in range(1, nExp):
        opCount[0] = 0
        gcd(m, n)
        totalOps += opCount[0]

    return totalOps/float(nExp)



if __name__ == "__main__":
    print "Solution 1 returns : %s"%(solve1([1,2,3,4]))
    print "Solution 4 returns : %s"%(solve4(2166, 6099))
    print "Solution 6 returns : %s"%(solve6(5, 10000))

