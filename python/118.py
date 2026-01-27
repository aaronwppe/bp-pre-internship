# Prog. 118
# Write a function to convert a string to a list.

import unittest


class TestStringToList(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_case_1(self):
        self.assertEqual(string_to_list("hello"), ["h", "e", "l", "l", "o"])


def string_to_list(string: str) -> list[str]:
    return [s for s in string]


if __name__ == "__main__":
    unittest.main()
