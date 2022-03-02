import unittest
import main


class TestMain(unittest.TestCase):

    def test_pale(self):

        self.assertEqual(main.palindrome_detector(
            given_string="pale"), False)

    def test_palest(self):

        self.assertEqual(main.palindrome_detector(
            given_string="palest"), False)

    def test_racecar(self):

        self.assertEqual(main.palindrome_detector(
            given_string="racecar"), True)

    

    


