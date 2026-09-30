from .image import read_ppm
from .planner import build_pick_list
from .segment import components


def analyze(path):
    width, height, pixels = read_ppm(path)
    detections = components(width, height, pixels)
    return {"detections": detections, "pick_list": build_pick_list(detections)}
