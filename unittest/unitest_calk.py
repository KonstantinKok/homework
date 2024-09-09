import calk
import unittest

class TestCalk(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calk.add(1,2),3)
    def test_sub(self):
        self.assertEqual(calk.sub(2,1),1)
    def test_mul(self):
        self.assertEqual(calk.mul(2,2),4)
    def test_div(self):
        self.assertEqual(calk.div(2,1),2)

if __name__ == '__main__':
    unittest.main()