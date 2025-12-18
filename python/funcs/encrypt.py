import random as rand

def create_enc_key():
    return rand.randint(1, 26)

def convert_key(key):
    return (26 - key) % 26

def enc_dec_text(text, key):
    letters_nums = {chr(97 + i): i % 26 for i in range(26)}
    nums_letters = {i % 26: chr(97 + i) for i in range(26)}

    result = ""
    for char in text:
        result += nums_letters[(letters_nums[char.lower()] + key) % 26] if char.isalpha() else char
    return result

def test_all():
    text = "Hello World!"
    key = create_enc_key()
    encrypted_text = enc_dec_text(text, key)
    converted_key = convert_key(key)
    decrypted_text = enc_dec_text(encrypted_text, converted_key)
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")

test_all()
