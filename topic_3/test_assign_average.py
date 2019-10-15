import unittest
from topic_3.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual('90', switch_average('A'))

    def test_b(self):
        self.assertEqual('80', switch_average('B'))

    def test_c(self):
        self.assertEqual('70', switch_average('C'))

    def test_d(self):
        self.assertEqual('60', switch_average('D'))

    def test_f(self):
        self.assertEqual('59', switch_average('F'))


if __name__ == '__main__':
    unittest.main()
