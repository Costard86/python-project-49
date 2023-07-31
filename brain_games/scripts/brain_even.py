from brain_games import engine
from brain_games.games import brain_even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.run_game(brain_even.play_even, description)


if __name__ == '__main__':
    main()
