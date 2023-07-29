import brain_games.engine
from random import randint

min_number = 1
max_number = 30
exercise = "Find the greatest common divisor of given numbers."


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand_numb1 = randint(min_number, max_number)
        rand_numb2 = randint(min_number, max_number)
        question = f'{rand_numb1}  {rand_numb2}'
        correct_answer = str(gcd(rand_numb1, rand_numb2))
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


def gcd(numb1: int, numb2: int) -> int:
    while numb1 != 0 and numb2 != 0:
        if numb1 > numb2:
            numb1 = numb1 % numb2
        else:
            numb2 = numb2 % numb1
    return numb1 + numb2


if __name__ == '__main__':
    main()
