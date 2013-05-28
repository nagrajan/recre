__author__ = 'nagarajan'

from math import log, e
import unittest

class Test_1_2_2(unittest.TestCase):
    def test_18(self, x=20):
        self.assertNotAlmostEqual(log(x, 8), 0.5*log(x, 2), delta = 0.000001)

    def test_19(self):
        print 47*log(2, 10)
        self.assertGreaterEqual(47*log(2,10), 14)

    def test_20(self):
        self.assertAlmostEqual(log(10, 2), 1.0/log(2, 10), delta=0.000001*log(10, 2))

    def test_22a(self):
        factor = log(10*e,2)/(log(e, 2)*log(10, 2))
        self.assertAlmostEqual(factor, 1, delta=0.01)

    def test_22b(self):
        data = range(2, 2000)
        error = 0
        for d in data:
            self.assertAlmostEqual(log(d, 2), (log(d) + log(d, 10)), delta=0.01*log(d, 2))
            error += abs(log(d, 2) - (log(d) + log(d, 10)))/log(d, 2)
        print 'Avg error = %s'%(error / len(data))

if __name__ == '__main__':
    unittest.main()