from brain_games import engine
from brain_games.games import brain_progression


def main():
    description = "What number is missing in the progression?"
    engine.run_game(brain_progression.play_progression, description)


if __name__ == '__main__':
    main()
