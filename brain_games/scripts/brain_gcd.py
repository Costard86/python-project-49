from brain_games import engine
from brain_games.games import brain_gcd


def main():
    description = 'Find the greatest common divisor of given numbers.'
    engine.run_game(brain_gcd.play_gcd, description)


if __name__ == '__main__':
    main()
