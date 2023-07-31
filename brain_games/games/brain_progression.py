from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 10
massive_elements = 10


def play_progression():
    first = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER + 1, MAX_NUMBER)
    random_miss_elem = randint(MIN_NUMBER, MAX_NUMBER - 1)
    progression = make_progression(first, step, massive_elements)
    correct_answer = str(progression[random_miss_elem])
    progression[random_miss_elem] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def make_progression(first: int, step: int, length: int) -> list:
    progression = []
    for i in range(length):
        progression.append(first)
        first = first + step
    return progression
