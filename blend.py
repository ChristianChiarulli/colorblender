from argparse import Namespace
from argparse import ArgumentParser
import re


import math


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    clean_hex: str = hex.replace("#", "")
    return tuple(int(clean_hex[i : i + 2], 16) for i in (0, 2, 4))


def blend(hex_fg: str, hex_bg: str, alpha: float) -> str:
    rgb_bg: tuple[int, int, int] = hex_to_rgb(hex_bg)
    rgb_fg: tuple[int, int, int] = hex_to_rgb(hex_fg)

    def blend_channel(channel: int) -> int:
        blended_channel: float = alpha * rgb_fg[channel] + (
            (1 - alpha) * rgb_bg[channel]
        )

        return math.floor(min(max(0, blended_channel), 255) + 0.5)

    def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb]
        )

    return rgb_to_hex((blend_channel(0), blend_channel(1), blend_channel(2)))


def validate_hex(input: str) -> bool:
    regex = "^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    pattern: re.Pattern[str] = re.compile(regex)

    if re.search(pattern, input):
        return True
    else:
        return False


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser("color blender")
    parser.add_argument("fg", help="forground", type=str)
    parser.add_argument("bg", help="background", type=str)
    parser.add_argument("alpha", help="alpha", type=float)
    args: Namespace = parser.parse_args()

    if args.alpha < 0 or args.alpha > 1:
        exit("alpha must be between 0 and 1")

    if validate_hex(args.fg) and validate_hex(args.bg):
        print(blend(args.fg, args.bg, args.alpha))
    else:
        print("invalid hex color")
        exit(1)
