import unittest
from topic_2.more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        the_dict = {'A': 95, 'B': 85, 'C': 75, 'D': 65, 'F': 59}
        check_item = 'B'
        self.assertEqual(True, dict_membership.in_dict(the_dict, check_item))

    def test_in_dict_false(self):
        the_dict = {'A': 95, 'B': 85, 'C': 75, 'D': 65, 'F': 59}
        check_item = 'E'
        self.assertEqual(False, dict_membership.in_dict(the_dict, check_item))


if __name__ == '__main__':
    unittest.main()
