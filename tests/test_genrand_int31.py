import os
import unittest

from mt19937ar import MT19937ar


class TestGenrandInt31(unittest.TestCase):
    def test_genrand_int31(self):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, "data/genrand_int31.txt")
        with open(filepath, "r") as f:
            testcases = f.read().strip().split("\n")

        mt = MT19937ar()
        mt.init_by_array([0x123, 0x234, 0x345, 0x456])
        for testcase in testcases:
            expected = int(testcase)
            self.assertEqual(mt.genrand_int31(), expected)
