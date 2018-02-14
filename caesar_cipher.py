def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    if unicode_value > 126:
        is_good = False
        unicode_value -= 32
        while not is_good:
            unicode_value -= 95
            if unicode_value <= 95:
                is_good = True
        unicode_value += 32
        
    elif unicode_value < 32:
        is_good = False
        unicode_value -= 32
        while not is_good:
            unicode_value += 95
            if unicode_value >= 0:
                is_good = True
        unicode_value += 32
        
    return chr(unicode_value)

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)

unencrypted_message = "Encryption is fun! Here are some numbers for testing purposes: 1357908642. OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOF! BACKSLASH \ qwertyuioplkjhgfdsazxcvbnm"
encrypted_message = encrypt(unencrypted_message, 10)
decrypted_message = decrypt(encrypted_message, 10)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

