import unittest
from Day1_SecretEntrance.SecretEntrance2 import calculate_code_sum


class TestSecretEntrance(unittest.TestCase):

    def test_on_zero_right(self):
        test_input='''R50'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_on_zero_left(self):
        test_input='''L50'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_from_zero_right(self):
            test_input = '''R50
    R50'''.splitlines()
            self.assertEqual(1, calculate_code_sum(test_input))

    def test_from_zero_left(self):
            test_input = '''L50
    L50'''.splitlines()
            self.assertEqual(1, calculate_code_sum(test_input))

    def test_overclick_right(self):
        test_input='''R60'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_overclick_left(self):
        test_input='''L99'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_above_hundered_right(self):
        test_input='''R110'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_above_hundered_left(self):
        test_input='''L149'''.splitlines()
        self.assertEqual(1,calculate_code_sum(test_input))

    def test_case1(self):
        test_input='''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''.splitlines()
        self.assertEqual(6,calculate_code_sum(test_input))

    def test_multiple_hundred_right(self):
        test_input='''R210'''.splitlines()
        self.assertEqual(2,calculate_code_sum(test_input))

    def test_multiple_hundred_left(self):
        test_input='''L249'''.splitlines()
        self.assertEqual(2,calculate_code_sum(test_input))

    def test_multiple_hundred_and_sum_right(self):
        test_input='''R251'''.splitlines()
        self.assertEqual(3,calculate_code_sum(test_input))

    def test_multiple_hundred_and_sum_left(self):
        test_input='''L251'''.splitlines()
        self.assertEqual(3,calculate_code_sum(test_input))

    def test_on_zero_with_hundred(self):
        test_input='''L550'''.splitlines()
        self.assertEqual(6,calculate_code_sum(test_input))

    def test_on_hundred_with_hundred(self):
        test_input='''R150'''.splitlines()
        self.assertEqual(2,calculate_code_sum(test_input))

    def test_secret_entrance2(self):
        with open("input.txt") as input_file:
            self.assertEqual(6684,calculate_code_sum(input_file))

if __name__ == "__main__":
    unittest.main()
