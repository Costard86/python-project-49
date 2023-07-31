from brain_games import engine
from brain_games.games import brain_calc


def main():
    description = 'What is the result of the expression?'
    engine.run_game(brain_calc.play_calc, description)


if __name__ == '__main__':
    main()
