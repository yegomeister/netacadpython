
def find():
    s1 = input('What letters are we looking for?\n')
    s2 = input('Where are we looking?\n')

    if s2.find(s1[0]):
        index_l = [s2.find(l, s2.find(s1[0]), len(s2)) for l in s1[1:]]
        print(index_l)
        return all(x > x+1 for x in range(len(index_l) - 2))
    else:
        return False


#print(find())
print('Yes' if find() else 'No')

# word = input()
# word = word.upper()



