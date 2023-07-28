import brain_games.engine
from random import randint

min_number = 1
max_number = 20
min_number_op = 0
max_number_op = 2
operators = ['+', '-', '*']
exercise = "What is the result of the expression?"


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand_numb1 = randint(min_number, max_number)
        rand_numb2 = randint(min_number, max_number)
        rand_operator = randint(min_number_op, max_number_op)
        operator = operators[rand_operator]
        question = f'{rand_numb1} {operator} {rand_numb2}'
        correct_answer = str(to_calc(rand_numb1, rand_numb2, operator))
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


def to_calc(num1, num2, operate):
    match operate:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case _: raise RuntimeError("Unknown operator: " + operate)


if __name__ == '__main__':
    main()