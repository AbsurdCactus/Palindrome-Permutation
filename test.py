import unittest
import main


class TestMain(unittest.TestCase):

    def test_pale_ple(self):

        self.assertEqual(main.palindrome_detector(
            string_one="pale", string_two="ple"), True)

    def test_pale_palest(self):

        self.assertEqual(main.palindrome_detector(
            string_one="pale", string_two="palest"), False)

    def test_pale_pa(self):

        self.assertEqual(main.palindrome_detector(
            string_one="pale", string_two="pa"), False)

    def test_pa_pale(self):
        self.assertEqual(main.palindrome_detector(
            string_one="pa", string_two="pale"), False)

    def test_pale_bale(self):
        self.assertEqual(main.palindrome_detector(
            string_one="pale", string_two="bale"), True)

    def test_pale_bane(self):

        self.assertEqual(main.palindrome_detector(
            string_one="pale", string_two="bane"), False)

    #there need to be a lot more tests


