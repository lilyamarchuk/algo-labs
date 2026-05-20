import unittest
from lab9 import fa_search


class TestFaSearch(unittest.TestCase):

    def test_single_occurrence(self):
        self.assertEqual(fa_search("hello world", "world"), [6])

    def test_multiple_occurrences(self):
        self.assertEqual(fa_search("ababab", "ab"), [0, 2, 4])

    def test_no_occurrence(self):
        self.assertEqual(fa_search("hello world", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(fa_search("hello", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(fa_search("", "abc"), [])

    def test_both_empty(self):
        self.assertEqual(fa_search("", ""), [])

    def test_needle_equals_haystack(self):
        self.assertEqual(fa_search("abc", "abc"), [0])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(fa_search("ab", "abcd"), [])

    def test_overlapping_pattern(self):
        self.assertEqual(fa_search("aaa", "aa"), [0, 1])

    def test_single_char_needle(self):
        self.assertEqual(fa_search("banana", "a"), [1, 3, 5])

    def test_case_sensitive(self):
        self.assertEqual(fa_search("Hello hello", "hello"), [6])

    def test_needle_at_start(self):
        self.assertEqual(fa_search("abcdef", "abc"), [0])

    def test_needle_at_end(self):
        self.assertEqual(fa_search("abcdef", "def"), [3])

    def test_repeated_single_char(self):
        self.assertEqual(fa_search("aaaa", "a"), [0, 1, 2, 3])

    def test_unicode(self):
        self.assertEqual(fa_search("привіт світ привіт", "привіт"), [0, 12])


if __name__ == "__main__":
    unittest.main()
