import ctypes
import os
import unittest

from mt19937ar import MT19937ar


class TestGenrandRes53(unittest.TestCase):
    def test_genrand_res53(self):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, "c/mt19937ar.so")

        c = ctypes.CDLL(filepath)
        c.init_by_array.argtypes = [ctypes.POINTER(ctypes.c_ulong), ctypes.c_int]
        c.init_by_array.restype = None
        c.genrand_res53.argtypes = []
        c.genrand_res53.restype = ctypes.c_double
        p = MT19937ar()

        seeds = [0x123, 0x234, 0x345, 0x456]
        c.init_by_array((ctypes.c_ulong * len(seeds))(*seeds), len(seeds))
        p.init_by_array(seeds)
        for _ in range(10000):
            result = p.genrand_res53()
            expected = c.genrand_res53()
            self.assertEqual(result, expected)