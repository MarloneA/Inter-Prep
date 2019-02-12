import unittest
from unittest.mock import patch

class Testguess(unittest.TestCase):

  def test_input(self):
    result = guesswork(3)
    self.assertEqual(result, "What's your guess?" )

  @patch(guesswork(1).get_input, return_value=1)
  def test_run(self):
    self.assertEqual(return_value=1,msg = "You got it")

  @patch(guesswork(9).get_input, return_value=4)
  def test_higher(self):
    self.input = "What's your guess?"
    self.output = random.randint(1,9)
    result = guesswork(int("9"))
    self.assertGreater(result,random.randint(1,9),msg ="Too high!")

  @patch(guesswork(9).get_input, return_value=2)
  def test_lower(self):
    self.input = "What's your guess?"
    self.output = random.randint(1,9)
    result = guesswork(int("9"))
    self.assertLess(result,random.randint(1,9),msg ="Too low!")
  
if __name__ == 'main':
  unittest.main()