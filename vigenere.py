class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _extend_key(self, text):
        extended_key = []
        key_length = len(self.key)
        key_index = 0  

        for char in text:
            if char.isalpha():  
                extended_key.append(self.key[key_index % key_length])
                key_index += 1 
            else:
                extended_key.append(char) 

        return ''.join(extended_key)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        extended_key = self._extend_key(plaintext)
        ciphertext = []

        for p, k in zip(plaintext, extended_key):
            if p.isalpha(): 
                shift = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
                ciphertext.append(chr(shift + ord('A')))
            else:
                ciphertext.append(p) 

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        extended_key = self._extend_key(ciphertext)
        plaintext = []

        for c, k in zip(ciphertext, extended_key):
            if c.isalpha(): 
                shift = (ord(c) - ord(k) + 26) % 26
                plaintext.append(chr(shift + ord('A')))
            else:
                plaintext.append(c)  

        return ''.join(plaintext)
