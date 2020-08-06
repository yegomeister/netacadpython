
def cipher(text):
    """Return a cipher of the user's text according to a shift value of 1 to 25"""
    try:
        sv = int(input('What is your desired shift value?'))
        if sv not in range(1, 26):
            print('Your shift value has to be between 1 and 25, nothing else')
            return cipher(text)
    except ValueError:
        print("Shift value can only be a number")
        return cipher(text)

    code = ''
    for char in text:
        if char.isalpha():
            val = ord(char) + sv
            if char.islower():
                code += chr(val) if val <= ord('z') else chr(ord('a') + (sv - 1))
            else:
                code += chr(val) if val <= ord('Z') else chr(ord('A') + (sv - 1))
        else:
            code += char

    return code


txt = input('Write a message to be encoded:\n')

print(cipher(txt))