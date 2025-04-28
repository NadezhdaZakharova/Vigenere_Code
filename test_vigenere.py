import unittest
from vigenere import VigenereCipher

class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("KEY")

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("HICAT"), "RMAKX")
    
    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("RMAKX"), "HICAT")

    def test_encrypt_with_spaces(self):
        self.assertEqual(self.cipher.encrypt("OH MY GOD"), "YL KI KMN")
    
    def test_decrypt_with_spaces(self):
        self.assertEqual(self.cipher.decrypt("YL KI KMN"), "OH MY GOD")

    def test_encrypt_with_non_alpha(self):
        self.assertEqual(self.cipher.encrypt("GO SLEEP!"), "QS QVICZ!")
    
    def test_decrypt_with_non_alpha(self):
        self.assertEqual(self.cipher.decrypt("QS QVICZ!"), "GO SLEEP!")

if __name__ == '__main__':
    unittest.main()
