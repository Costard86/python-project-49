import brain_games.engine
from random import randint

min_number = 1
max_number = 100
exercise = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand = randint(min_number, max_number)
        correct_answer = 'yes' if rand % 2 == 0 else 'no'
        question = str(rand)
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


if __name__ == '__main__':
    main()
