def mysplit(strng):
    """A replica of python's built-in split() method"""
    lst = []
    word = ''
    for ch in strng:
        if ch != ' ':
            word += ch
        elif word != '':
            lst.append(word)
            word = ''
            continue

    if word != '':
        lst.append(word)
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))