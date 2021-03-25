def anagram():
    """This function checks whether two given words are anagrams i.e. made of the same letters"""
    w1 = input("Enter the first text: ").lower()
    w2 = input("Enter the second text: ").lower()

    return sorted(''.join(w1.split())) == sorted(''.join(w2.split()))

if anagram():
    print("Anagrams")
else:
    print("Not anagrams")