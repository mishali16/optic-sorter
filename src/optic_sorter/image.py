from pathlib import Path


def read_ppm(path):
    tokens = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        clean = line.split("#", 1)[0].strip()
        if clean:
            tokens.extend(clean.split())
    if tokens[:1] != ["P3"]:
        raise ValueError("expected ASCII PPM image starting with P3")
    width, height, max_value = map(int, tokens[1:4])
    if max_value != 255:
        raise ValueError("only max value 255 is supported")
    values = list(map(int, tokens[4:]))
    if len(values) != width * height * 3:
        raise ValueError("pixel data does not match image size")
    pixels = [(values[i], values[i + 1], values[i + 2]) for i in range(0, len(values), 3)]
    return width, height, pixels
