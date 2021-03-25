def digitoflife():
    birth = input("Enter your birthday in the format: YYYYMMDD/ YYYYDDMM/ MMDDYYY: ")
    while len(birth) > 1:
        birth = str(sum([int(i) for i in birth]))
    print("Your digit of life is:", birth)

digitoflife()