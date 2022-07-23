import math

# convert hex to rgb
def hex_to_rgb(hex):
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def blend(fg, bg, alpha):
    bg = hex_to_rgb(bg)
    fg = hex_to_rgb(fg)

    def blend_channel(i):
        ret = alpha * fg[i] + ((1 - alpha) * bg[i])

        return math.floor(min(max(0, ret), 255) + 0.5)

    def rgb_to_hex(rgb):
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb]
        )

    return rgb_to_hex((blend_channel(0), blend_channel(1), blend_channel(2)))


print(blend("de4b4b", "1e222a", 0.1))
print(blend("eaaf58", "1e222a", 0.1))
print(blend("1dbc9b", "1e222a", 0.1))
print(blend("4ac1fe", "1e222a", 0.1))
