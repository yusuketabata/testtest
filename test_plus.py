import unittest
from plus import plus

class TestPlus(unittest.TestCase):
    def test_int(self):
        self.assertEqual(plus(1,2),3,"error on int")

unittest.main()
