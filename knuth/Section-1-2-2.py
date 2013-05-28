__author__ = 'nagarajan'

def findLogBase10(x, accu=20):
    # no negative numbers allowed
    if x < 0:
        return None

    n = 0
    if x > 10:
        while x > 10:
            n += 1
            x = x / 10.0
    elif x < 1:
        while x < 1:
            n -= 1
            x = x * 10.0
    elif x == 1:
        return 0


    # process x to get 20 decimal places of accuracy
    bits = []
    idx1 = 0
    while idx1 < accu:
        x = x*x
        if x >= 10:
            x = x / 10.0
            bits.append(1)
        else:
            bits.append(0)
        idx1 += 1

    return n, bits

def decipherBitStream(bits):
    result = 0
    for i, b in enumerate(bits):
        if b == 1:
            result += pow(2, -1-i)
    return result


if __name__ == '__main__':
    n, bits = findLogBase10(2)

    number = n + decipherBitStream(bits)
    print bits
    print number
