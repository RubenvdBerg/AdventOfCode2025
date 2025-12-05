import unittest
from Day3_Lobby.Lobby1 import calculate_solution1
from Day3_Lobby.Lobby2 import calculate_solution

class TestLobby(unittest.TestCase):
    test_data='''987654321111111
811111111111119
234234234234278
818181911112111
'''.splitlines()

    def test_example1(self):
        self.assertEqual(357, calculate_solution1(self.test_data))

    def test_example2(self):
        self.assertEqual(3121910778619, calculate_solution(self.test_data))

if __name__ == "__main__":
    unittest.main()
