# def make_board
# def set_hex_colours
# def set_all_pieces
# def place_players_pieces
# def place_piece

# TODO Make a list of all positions to Hexes e.g. [Position(0,-1,3): Hex]


import sys


def info(msg: str):
    print(f"{msg}", file=sys.stderr, flush=True)


def warn(msg: str):
    print(f"warning: {msg}", file=sys.stderr, flush=True)


def die(msg: str):
    print(f"error: {msg}", file=sys.stderr, flush=True)
    sys.exit(1)


def make_board():
    raise NotImplementedError


def main():
    print("Want to Play Hex Chess?!")


if __name__ == "__main__":
    main()
