def led():
    segs = [('  #', '  #', '  #', '  #', '  #'), ('###', '  #', '###', '#  ', '###'),
            ('###', '  #', '###', '  #', '###'), ('# #', '# #', '###', '  #', '  #'),
            ('###', '#  ', '###', '  #', '###'), ('###', '#  ', '###', '# #', '###'),
            ('###', '  #', '  #', '  #', '  #'), ('###', '# #', '###', '# #', '###'),
            ('###', '# #', '###', '  #', '###'), ('###', '# #', '# #', '# #', '###')]

    number = input('Enter a number to display its 7-segment value: ')
    try:
        trial = int(number)
    except ValueError:
        print('Hmm that\'s not exactly a number. Let\'s try again')
        return led()
    if int(number) < 0:
        print('We\'re gonna limit this to positive numbers. Try again?')
        return led()
    else:
        for i in range(5):
            print('  '.join(segs[int(dig) - 1][i] for dig in number))

led()



