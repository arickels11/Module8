import unittest
from topic_4 import half_birthday
import datetime

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2019, 3, 7)
        expected_hbd = 9/7/219
        self.assertEqual(expected_hbd, half_birthday.half_birthday(birthday))


if __name__ == '__main__':
    unittest.main()
