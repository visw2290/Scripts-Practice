import unittest

class Check(unittest.TestCase):
    def test_check_value(self):
        self.assertEqual(5,2+3)
    def test_check_random(self):
        self.assertEqual(10,15-5)
    @unittest.skip('WEP')
    def test_check_word(self):
        self.assertEquals(10,5+6)