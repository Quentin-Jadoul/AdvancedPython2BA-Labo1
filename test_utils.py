# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5), 120)
        self.assertEqual(utils.fact(0), 1)
        self.assertFalse(utils.fact(-4))
    
    def test_roots(self):
        self.assertEqual(utils.roots(1, 0, 1), ())
        self.assertEqual(utils.roots(1, 1, 0), (0, -1))
        self.assertEqual(utils.roots(1, 0, 0), (0))
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
