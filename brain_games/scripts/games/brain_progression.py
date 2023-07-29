import brain_games.engine
from random import randint

min_number = 1
max_number = 10
massive_elements = 10
exercise = "What number is missing in the progression?"


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        first = randint(min_number, max_number)
        step = randint(min_number + 1, max_number)
        random_miss_elem = randint(min_number, max_number - 1)
        progression = make_progression(first, step, massive_elements)
        correct_answer = str(progression[random_miss_elem])
        progression[random_miss_elem] = '..'
        question = ' '.join(map(str, progression))
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


def make_progression(first: int, step: int, length: int) -> list:
    progression = []
    for i in range(length):
        progression.append(first)
        first = first + step
    return progression


if __name__ == '__main__':
    main()