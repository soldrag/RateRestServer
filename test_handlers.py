import unittest
from handler import json_compiler, args_parser
import json


class TestJsonCompiler(unittest.TestCase):

    def setUp(self) -> None:
        self.json_compiler = json_compiler
        self.valid_json = json.dumps(
            {
                'currency': 'USD',
                'rate': 68.50,
                'request_value': 100,
                'converted_value': 6850.0
            }
        )

    def test_valid_values(self):
        self.assertEqual(self.json_compiler('USD', 68.50, 100, 6850.0), self.valid_json)

    def test_negative_request1(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', -68.50, 100, 6850.0)

    def test_negative_request2(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', 68.50, -100, 6850.0)

    def test_negative_request3(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', 68.50, 100, -6850.0)


class TestArgParser(unittest.TestCase):

    def setUp(self) -> None:
        self.arg_parser = args_parser
        self.full_valid_path = '/rest/convert?value=100&currency=EUR'
        self.valid_path = '/rest/convert?value=100'
        self.invalid_value = '/rest/convert?value=10t'
        self.no_value = '/rest/convert?valu=100'

    def test_valid_path1(self):
        self.assertEqual(self.arg_parser(self.full_valid_path), ('EUR', 100))

    def test_valid_path2(self):
        self.assertEqual(self.arg_parser(self.valid_path), ('USD', 100))

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            self.arg_parser(self.invalid_value)

    def test_no_value(self):
        with self.assertRaises(KeyError):
            self.arg_parser(self.no_value)


if __name__ == '__main__':
    unittest.main()
