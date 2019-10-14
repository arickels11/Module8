import unittest
from topic_4 import half_birthday
import datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        expected_hbd = "2019-09-07 00:00:00"
        self.assertEqual(expected_hbd, half_birthday.half_birthday(2019, 3, 7))


if __name__ == '__main__':
    unittest.main()
