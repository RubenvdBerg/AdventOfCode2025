import unittest
from Day2_GiftShop.GiftShop1 import calculate_id_sum1
from Day2_GiftShop.GiftShop2 import calculate_id_sum

class TestGiftShop(unittest.TestCase):
    test_data='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

    def test_example1(self):
        self.assertEqual(1227775554, calculate_id_sum1(self.test_data))

    def test_example2(self):
        self.assertEqual(4174379265, calculate_id_sum(self.test_data))

if __name__ == "__main__":
    unittest.main()
