# Optic Sorter

Computer vision toy that detects colored parts in a simple image and turns them into a robot pick list.

Small robotics projects often need perception code that is understandable before it is powerful. Optic Sorter reads a tiny PPM image, groups colored regions, classifies them as parts, bins, or hazards, and outputs structured pick actions.

```bash
PYTHONPATH=src python3 -m optic_sorter samples/workcell.ppm
PYTHONPATH=src python3 -m unittest discover -s tests
```

## How It Works

```mermaid
flowchart LR
  A[PPM image] --> B[Color segmentation]
  B --> C[Connected regions]
  C --> D[Part classifier]
  D --> E[Pick list JSON]
```

The local detector uses flood fill over color masks. It is deliberately dependency-free so the repo is easy to run on a laptop or Raspberry Pi before swapping in OpenCV.

## Architecture

- `image.py`: ASCII PPM loader
- `segment.py`: color thresholding and connected components
- `planner.py`: converts detections into pick, place, inspect, and avoid actions
- `cli.py`: command-line JSON output

## Demo

```bash
PYTHONPATH=src python3 -m optic_sorter samples/workcell.ppm
```

Example output:

```json
{
  "detections": [{"label": "red_part", "center": [2, 2], "area": 4}],
  "pick_list": [{"action": "pick", "target": "red_part", "destination": "red_bin"}]
}
```

## Why I Built This

I wanted a computer-vision project that connects directly to robotics instead of stopping at detection. The interesting part is the interface between pixels and robot actions.

## Future Ideas

- OpenCV camera adapter
- FTC telemetry output
- Calibration from real field images
- Gripper-safe path constraints

## GitHub

Description: Dependency-free vision pipeline that turns colored parts into a robot pick list.

Topics: `computer-vision`, `robotics`, `python`, `raspberry-pi`, `image-processing`, `ftc`
