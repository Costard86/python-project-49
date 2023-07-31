from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 80


def play_prime():
    rand_numb = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(rand_numb)
    correct_answer = 'yes' if is_prime(rand_numb) else 'no'
    return question, correct_answer


def is_prime(numb: int) -> bool:
    if numb < 2:
        return False
    divider = 2
    while divider <= numb / 2:
        if numb % divider == 0:
            return False
        divider += 1
    return True
