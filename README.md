# Описание
Данная программа реализует шифр Виженера. Можно использовать пробелы и спецсимволы.

# Запуск программы
Скачайте все файлы с кодом. Откройте терминал или командную строку. Перейдите в директорию с загруженным кодом.
Запустите Python интерпретатор и импортируйте класс VigenereCipher:

from vigenere import VigenereCipher

cipher = VigenereCipher("YOURKEY")
encrypted_text = cipher.encrypt("YOURPLAINTEXT")
decrypted_text = cipher.decrypt(encrypted_text)
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")

# Тестирование
Запуск тестов из командной строки:

python -m unittest test_vigenere.py

# Примечание
При желании YOURKEY и YOURPLAINTEXT можно заменить.