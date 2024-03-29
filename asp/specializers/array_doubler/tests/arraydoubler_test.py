import unittest

from array_doubler import *

class BasicTests(unittest.TestCase):
    def test_pure_python(self):
        arr = [1.0,2.0,3.0]
        result = ArrayDoubler().double(arr)
        self.assertEquals(result[0], 2.0)

    def test_generated(self):
        arr = [1.0, 2.0, 3.0]
        arr2 = [2.0, 3.0, 4.0]
        result = ArrayDoubler().double_using_template(arr)
        
        result2 = ArrayDoubler()double_using_template(arr2)
        self.assertEquals(result[0], 2.0)


if __name__ == '__main__':
    unittest.main()
