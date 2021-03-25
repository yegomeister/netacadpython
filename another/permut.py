"""permutation function"""
import random

def permut(lst, sample):
    return_list = []
    while len(return_list) < sample:
        perm = set(random.choices(population=lst, k=sample))

        if perm not in return_list:
            return_list.append(perm)

    return return_list

list_of_nums = [23, 51, 44, 56, 7, 88, 99, 545, 232, 11, 15, 66, 77, 89, 35, 61, 151, 72]

prompt = "I have", len(list_of_nums), "number of items. What is your sample size of items to pick?"
sample = int(input(prompt))
perm = permut(list_of_nums, sample)
outcomes = sum(len(pick) for pick in perm)

