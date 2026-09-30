from collections import deque


RULES = {
    "red_part": lambda r, g, b: r > 180 and g < 90 and b < 90,
    "green_bin": lambda r, g, b: g > 160 and r < 100 and b < 120,
    "blue_part": lambda r, g, b: b > 160 and r < 120 and g < 130,
    "yellow_hazard": lambda r, g, b: r > 170 and g > 150 and b < 100,
}


def classify(pixel):
    for label, rule in RULES.items():
        if rule(*pixel):
            return label
    return None


def components(width, height, pixels, min_area=2):
    labels = [classify(pixel) for pixel in pixels]
    seen = set()
    found = []
    for start, label in enumerate(labels):
        if label is None or start in seen:
            continue
        region = flood(start, label, labels, width, height, seen)
        if len(region) >= min_area:
            xs = [i % width for i in region]
            ys = [i // width for i in region]
            found.append(
                {
                    "label": label,
                    "center": [sum(xs) // len(xs), sum(ys) // len(ys)],
                    "bbox": [min(xs), min(ys), max(xs), max(ys)],
                    "area": len(region),
                }
            )
    return sorted(found, key=lambda item: (item["label"], item["center"]))


def flood(start, label, labels, width, height, seen):
    queue = deque([start])
    seen.add(start)
    region = []
    while queue:
        index = queue.popleft()
        region.append(index)
        x, y = index % width, index // width
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                neighbor = ny * width + nx
                if neighbor not in seen and labels[neighbor] == label:
                    seen.add(neighbor)
                    queue.append(neighbor)
    return region
