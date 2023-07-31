import prompt


ROUND_COUNT = 3


def run_game(game, description):
    print("Welcome to the Brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)
    for _ in range(ROUND_COUNT):
        (question, correct_answer) = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
