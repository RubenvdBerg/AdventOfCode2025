import unittest
from Day4_PrintingDepartment.PrintingDepartment1 import calculate_solution1
from Day4_PrintingDepartment.PrintingDepartment2 import calculate_solution

class TestPrintingDepartment(unittest.TestCase):
    test_data='''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

    def test_example1(self):
        self.assertEqual(13, calculate_solution1(self.test_data))

    def test_example2(self):
        self.assertEqual(43, calculate_solution(self.test_data))

if __name__ == "__main__":
    unittest.main()
