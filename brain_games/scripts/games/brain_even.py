import brain_games.engine
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
exercise = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = 'yes' if rand % 2 == 0 else 'no'
        question = str(rand)
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


if __name__ == '__main__':
    main()
