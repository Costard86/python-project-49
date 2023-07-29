import brain_games.engine
from random import randint

min_number = 1
max_number = 80
exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    attempts = 0
    quest_and_ans = []
    while attempts < brain_games.engine.ROUND_COUNT:
        rand_numb = randint(min_number, max_number)
        question = str(rand_numb)
        correct_answer = 'yes' if is_prime(rand_numb) else 'no'
        quest_and_ans.append((question, correct_answer))
        attempts += 1
    brain_games.engine.game_run(quest_and_ans, exercise)


def is_prime(numb: int) -> bool:
    if numb < 2:
        return False
    divider = 2
    while divider <= numb / 2:
        if numb % divider == 0:
            return False
        divider += 1
    return True


if __name__ == '__main__':
    main()
