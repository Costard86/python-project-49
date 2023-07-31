from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 20
MIN_NUMBER_OP = 0
MAX_NUMBER_OP = 2
operators = ['+', '-', '*']


def play_calc():
    rand_numb1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_numb2 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_operator = randint(MIN_NUMBER_OP, MAX_NUMBER_OP)
    operator = operators[rand_operator]
    question = f'{rand_numb1} {operator} {rand_numb2}'
    correct_answer = str(to_calc(rand_numb1, rand_numb2, operator))
    return question, correct_answer


def to_calc(num1: int, num2: int, operate: str) -> int:
    match operate:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case _: raise RuntimeError("Unknown operator: " + operate)
