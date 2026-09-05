from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd


def csv_to_candlestick_image(
    csv_path: Path,
    output_path: Path,
) -> None:
    """
    Convert an OHLCV CSV file into a candlestick chart PNG.
    """

    df = pd.read_csv(csv_path)

    # Create a synthetic datetime index.
    df["Date"] = pd.date_range(
        start="2026-01-01",
        periods=len(df),
        freq="D",
    )

    df.set_index("Date", inplace=True)

    # mplfinance expects these exact column names.
    df = df.rename(
        columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume",
        }
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Create the candlestick chart.
    mpf.plot(
        df,
        type="candle",
        style="charles",
        volume=False,
        axisoff=True,
        figsize=(4, 4),
        savefig=dict(
            fname=str(output_path),
            dpi=150,
            bbox_inches="tight",
            pad_inches=0,
        ),
        closefig=True,
    )


def render_dataset(
    input_dir: Path,
    output_dir: Path,
) -> None:
    """
    Convert all CSV files in the dataset into PNG images.
    """

    for pattern_dir in input_dir.iterdir():

        if not pattern_dir.is_dir():
            continue

        pattern = pattern_dir.name

        print(f"Rendering {pattern}...")

        output_pattern_dir = output_dir / pattern

        csv_files = sorted(pattern_dir.glob("*.csv"))

        for csv_file in csv_files:

            output_file = (
                output_pattern_dir
                / f"{csv_file.stem}.png"
            )

            csv_to_candlestick_image(
                csv_path=csv_file,
                output_path=output_file,
            )

    print("Chart rendering complete.")