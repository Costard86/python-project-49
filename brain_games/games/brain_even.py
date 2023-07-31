from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100


def play_even():
    rand = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if rand % 2 == 0 else 'no'
    question = str(rand)
    return question, correct_answer
