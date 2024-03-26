import unittest
def add(a,b):
    return a+b
class TestAdd(unittest.TestCase):
    def test_add(self):
        result=add(12,10)
        self.assertEqual(result, 22)
if __name__=='__main__':
    unittest.main()