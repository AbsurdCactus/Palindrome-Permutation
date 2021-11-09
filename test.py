import unittest
import main

class TestMain(unittest.TestCase):

    def test_pale_ple(self):

        self.assertTrue(main.palindrome_detector(string_one="pale", string_two="ple"), True)

     # this should not be working yet   
    def test_pale_bake(self):

         self.assertTrue(main.palindrome_detector(string_one="pale", string_two="bake"), False)

        