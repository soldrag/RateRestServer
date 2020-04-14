import unittest
from handler import json_compiler
import json


class TestJsonCompiler(unittest.TestCase):

    def setUp(self) -> None:
        self.json_compiler = json_compiler
        self.good_values = json.dumps(
            {
                'currency': 'USD',
                'rate': 68.50,
                'request_value': 100,
                'converted_value': 6850.0
            }
        )

    def test_good_values(self):
        self.assertEqual(self.json_compiler('USD', 68.50, 100, 6850.0), self.good_values)

    def test_negative_request1(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', -68.50, 100, 6850.0)

    def test_negative_request2(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', 68.50, -100, 6850.0)

    def test_negative_request3(self):
        with self.assertRaises(ValueError):
            self.json_compiler('USD', 68.50, 100, -6850.0)


if __name__ == '__main__':
    unittest.main()
