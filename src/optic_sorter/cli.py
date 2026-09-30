import argparse
import json

from .pipeline import analyze


def main():
    parser = argparse.ArgumentParser(description="Detect colored parts and build a robot pick list.")
    parser.add_argument("image")
    args = parser.parse_args()
    print(json.dumps(analyze(args.image), indent=2))


if __name__ == "__main__":
    main()
