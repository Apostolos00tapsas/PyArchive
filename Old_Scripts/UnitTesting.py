import unittest

class TestWhatever(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, 0)
    def test_ones(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()