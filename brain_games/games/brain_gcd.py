from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 30


def play_gcd():
    rand_numb1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_numb2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{rand_numb1} {rand_numb2}'
    correct_answer = str(gcd(rand_numb1, rand_numb2))
    return question, correct_answer


def gcd(numb1: int, numb2: int) -> int:
    while numb1 != 0 and numb2 != 0:
        if numb1 > numb2:
            numb1 = numb1 % numb2
        else:
            numb2 = numb2 % numb1
    return numb1 + numb2
