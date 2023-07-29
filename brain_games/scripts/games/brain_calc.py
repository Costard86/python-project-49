import brain_games.engine
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 20
MIN_NUMBER_OP = 0
MAX_NUMBER_OP = 2
operators = ['+', '-', '*']
exercise = "What is the result of the expression?"


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand_numb1 = randint(MIN_NUMBER, MAX_NUMBER)
        rand_numb2 = randint(MIN_NUMBER, MAX_NUMBER)
        rand_operator = randint(MIN_NUMBER_OP, MAX_NUMBER_OP)
        operator = operators[rand_operator]
        question = f'{rand_numb1} {operator} {rand_numb2}'
        correct_answer = str(to_calc(rand_numb1, rand_numb2, operator))
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


def to_calc(num1: int, num2: int, operate: str) -> int:
    match operate:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case _: raise RuntimeError("Unknown operator: " + operate)


if __name__ == '__main__':
    main()
