def mysplit(strng):
    lst = []
    word = ''
    for ch in strng:
        if ch != ' ':
            word += ch
        elif ch == ' ':
            if word != '':
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