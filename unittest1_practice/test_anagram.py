import unittest
import anagram

class TestIsAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.is_anagram("sort","rost"),True)  #is_anagram("sort","rost"),True)

if __name__ == '__main__':
    unittest.main() 