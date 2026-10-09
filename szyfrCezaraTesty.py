import unittest
from szyfrCezara import szyfrCezaraTekst

class TestySzyfruCezara(unittest.TestCase):
    def test_abc_equal_def(self):
        self.assertEqual(szyfrCezaraTekst(3,"abc"), 'def')
    def test_xyz_equal_abc(self):
        self.assertEqual(szyfrCezaraTekst(3,"xyz"), "abc")
    def test_def_equal_abc(self):
        self.assertEqual(szyfrCezaraTekst(-3,"def"), "abc")
    def test_abc_equal_def_more_than_alphabet_length(self):
        self.assertEqual(szyfrCezaraTekst(29,"abc"), "def")
    def test_with_space_in_test(self):
        self.assertNotEqual(szyfrCezaraTekst(2,"ab cd"), "cd ef")
if __name__ == '__main__':
    unittest.main()
