import math

# convert hex to rgb
def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def blend(hex_fg: str, hex_bg: str, alpha: float) -> str:
    rgb_bg: tuple[int, int, int] = hex_to_rgb(hex_bg)
    rgb_fg: tuple[int, int, int] = hex_to_rgb(hex_fg)

    def blend_channel(channel: int) -> int:
        blended_channel: float = alpha * rgb_fg[channel] + ((1 - alpha) * rgb_bg[channel])

        return math.floor(min(max(0, blended_channel), 255) + 0.5)

    def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb]
        )

    return rgb_to_hex((blend_channel(0), blend_channel(1), blend_channel(2)))


print(blend("de4b4b", "1e222a", 0.1))
print(blend("eaaf58", "1e222a", 0.1))
print(blend("1dbc9b", "1e222a", 0.1))
print(blend("4ac1fe", "1e222a", 0.1))
