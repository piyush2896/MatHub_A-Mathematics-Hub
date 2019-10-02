import unittest

import arithmetic_api
from arithmetic_api import basic_ops

class TestBasicOps(unittest.TestCase):

    @staticmethod
    def add_data():
        data_list = [
            ({
                'operand1': 12,
                'operand2': 15,
                'operator': '+'
            }, 27),
            ({
                'operand1': -1,
                'operand2': -1,
                'operator': '+'
            }, -2),
            ({
                'operand1': -1,
                'operand2': 1,
                'operator': '+'
            }, 0)
        ]
        return data_list

    @staticmethod
    def sub_data():
        data_list = [
            ({
                'operand1': 12,
                'operand2': 15,
                'operator': '-'
            }, -3),
            ({
                'operand1': -1,
                'operand2': -2,
                'operator': '-'
            }, 1),
            ({
                'operand1': -1,
                'operand2': 9,
                'operator': '-'
            }, -10)
        ]
        return data_list

    def test_add(self):
        data_list = TestBasicOps.add_data()
        for data, expected in data_list:
            self.assertEqual(basic_ops.add(data), expected)

    def test_sub(self):
        data_list = TestBasicOps.sub_data()
        for data, expected in data_list:
            self.assertEqual(basic_ops.sub(data), expected)
