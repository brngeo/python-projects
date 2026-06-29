def atbash(text):
    result = ''
    for char in text:
        if char.isalpha():
            offset = ord(char.upper()) - ord('A')
            result += chr(ord('Z') - offset)
        else:
            result += char
    return result
print(atbash("Brian Geoffrey"))
