import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SPECIAL = '~!@#$%^&*()_+'

def generatePassword(length):
    if length < 1:
        length = 6
    passwordList = []
    #first assign the mandatory
    passwordList.append(LOWER_LETTERS[random.randint(0,25)])
    passwordList.append(UPPER_LETTERS[random.randint(0,25)])
    passwordList.append(NUMBERS[random.randint(0,9)])
    passwordList.append(SPECIAL[random.randint(0,11)])
    #now fill rest with random
    allStrings = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    remLen = length - 4
    while len(passwordList) < length:
        passwordList.append(allStrings[random.randint(0,74)])

    # shuffle passwordList
    random.shuffle(passwordList)

    #return as string
    return ''.join(passwordList)