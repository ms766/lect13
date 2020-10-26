import unittest
from hw13 import my_func

class TestMy_func(unittest.TestCase):
    def test_my_func(self):
  
        self.assertAlmostEqual(my_func(1,1,1.0),'counter is 10')
        # self.assertAlmostEqual(my_func(10,1,1),'counter is 10')
        # self.assertAlmostEqual(my_func(1,1,10),'counter is 10')
        # self.assertAlmostEqual(my_func(10,10,10),'counter is 10')
        # self.assertAlmostEqual(my_func(9,9,9),'counter is 10')
    
    
        self.assertEqual(my_func(0, 0, 0), 'Dont iterate')
        self.assertEqual(my_func(1, 0, 0), 'initial is 0')
        