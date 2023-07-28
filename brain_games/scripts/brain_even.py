import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        rand = randint(1, 100)
        true_answer = 'yes' if rand % 2 == 0 else 'no'
        print(f'Question: {rand}')
        ans = prompt.string('Your answer: ')
        if ans != true_answer:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
