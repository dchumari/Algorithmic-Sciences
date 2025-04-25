import unittest
from server import search_in_file

class TestServer(unittest.TestCase):
    def test_empty_query(self):
        self.assertEqual(search_in_file(""), "STRING NOT FOUND\n")

    def test_valid_query(self):
        self.assertEqual(search_in_file("test_string"), "STRING EXISTS\n")

    def test_oversized_payload(self):
        with self.assertRaises(ValueError):
            search_in_file("a" * 1025)

    def test_null_bytes(self):
        self.assertEqual(search_in_file("\x00test_string\x00"), "STRING NOT FOUND\n")

    def test_malformed_input(self):
        self.assertEqual(search_in_file("   "), "STRING NOT FOUND\n")

if __name__ == "__main__":
    unittest.main()