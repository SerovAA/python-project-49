#!/usr/bin/env python3
from brain_games.engine import run_brain_game
from brain_games.games import gcd


def main():
    run_brain_game(gcd)


if __name__ == '__main__':
    main()
