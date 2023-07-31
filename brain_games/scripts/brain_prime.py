from brain_games import engine
from brain_games.games import brain_prime


def main():
    description = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')
    engine.run_game(brain_prime.play_prime, description)


if __name__ == '__main__':
    main()
