from pathlib import Path

from generators.chart_renderer import render_dataset


INPUT_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/images")


def main() -> None:
    render_dataset(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
    )


if __name__ == "__main__":
    main()