def palindrome():
    text = input("What are we checking?\n")
    test = ''.join(text.split()).lower()

    for i in range(len(test)//2):
        if test[i] != test[(-1 - i)]:
            return False
        return True

if palindrome():
    print("It's a palindrome")
else:
    print("It's not a palindrome")
