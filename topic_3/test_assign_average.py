import unittest
from topic_3.assign_average import get_grade


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(90, get_grade('A'))

    def test_b(self):
        self.assertEqual(80, get_grade('B'))

    def test_c(self):
        self.assertEqual(70, get_grade('C'))

    def test_d(self):
        self.assertEqual(60, get_grade('D'))

    def test_f(self):
        self.assertEqual(59, get_grade('F'))

    def test_none(self):
        self.assertEqual('none', get_grade('E'))


if __name__ == '__main__':
    unittest.main()
