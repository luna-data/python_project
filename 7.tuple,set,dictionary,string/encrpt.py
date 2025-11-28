def encrypt(text, shift):
    encrypted_text = ""
    for char in text :
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                encrypted_code = ((char_code - ord('a') + shift) % 26) + ord('a')
            else:
                encrypted_code = ((char_code - ord('A') + shift) % 26) + ord('A')
            encrypted_char = chr(encrypted_code)
            encrypted_text = encrypted_char
        else:
            encrypted_text = char
    return encrypted_text

input_text = input("암호화할 문자열을 입력하시오 : ")
shift_amount = int(input("암호화에 사용할 시프트값을 입력하시오 (양수 또는 음수) : "))

encrypted_text = encrypt(input_text, shift_amount)
print("암호화된 문자열 :", encrypted_text)