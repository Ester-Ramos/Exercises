import unittest
from compression import compress_string

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(compress_string("aabccccaaa"), "a2b1c4a3")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string(None), None)
        self.assertEqual(compress_string("abcd"), "abcd")
        self.assertEqual(compress_string("aafffddooo"), "a2f3d2o3")



if __name__ == "__main__":
    unittest.main()
