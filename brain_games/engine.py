import prompt


ROUND_COUNT = 3


def game_run(questions_and_answers, exercise):
    print("Welcome to the Brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(exercise)
    for question, correct_answer in questions_and_answers:
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}')
