import unittest

class Testelevator(unittest.TestCase):

  def test_invalid(self):
    result = elevator(0,1,3)
    self.assertEqual(result,'Invalid call' )
  def test_elevator(self):
    
    result = elevator(0,1,0)
    self.assertEqual(result, "left" )
    result1 = elevator(0,1,1)
    self.assertEqual(result, "right" )
    result2 = elevator(0,1,2)
    self.assertEqual(result, "right" )
    result3 = elevator(0,0,0)
    self.assertEqual(result, "right" )
    result4 = elevator(0,2,1)
    self.assertEqual(result, "right" )
  
if __name__ == 'main':
  unittest.main()