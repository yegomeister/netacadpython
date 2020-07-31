def readint(prompt, minimum, maximum):
    """Test for an integer input and check whether it is within the min and max ranges defined"""
    try:
        number = int(input(prompt))
        if number in range(minimum, maximum):
            return number
        else:
            print('Error: the value', number, 'is not within permitted range', minimum, 'to', maximum)
            return readint(prompt, minimum, maximum)
    except ValueError:
        print('Error: invalid input')
    return readint(prompt, minimum, maximum)