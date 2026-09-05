import csv
import random
from pathlib import Path

from generators.ohlcv import generate_market_sequence
from generators.patterns import (
    PatternType,
    create_bullish_engulfing,
    create_bearish_engulfing,
    create_doji,
)


NUM_SAMPLES_PER_CLASS = 25
NUM_BACKGROUND_CANDLES = 48

OUTPUT_DIR = Path("data/raw")


def save_sample(
    sample_id: int,
    pattern: PatternType,
) -> None:

    # Generate normal market data
    candles = generate_market_sequence(
        num_candles=NUM_BACKGROUND_CANDLES,
        starting_price=random.uniform(50, 500),
    )

    previous_close = candles[-1].close

    # Add the target pattern
    if pattern == PatternType.BULLISH_ENGULFING:
        pattern_candles = create_bullish_engulfing(previous_close)

    elif pattern == PatternType.BEARISH_ENGULFING:
        pattern_candles = create_bearish_engulfing(previous_close)

    elif pattern == PatternType.DOJI:
        pattern_candles = create_doji(previous_close)

    elif pattern == PatternType.NO_PATTERN:
        pattern_candles = []

    else:
        raise ValueError(f"Unsupported pattern: {pattern}")

    candles.extend(pattern_candles)

    # Create output directory
    output_dir = OUTPUT_DIR / pattern.value
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{sample_id:05d}.csv"

    with output_file.open("w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "open",
            "high",
            "low",
            "close",
            "volume",
        ])

        for candle in candles:
            writer.writerow([
                candle.open,
                candle.high,
                candle.low,
                candle.close,
                candle.volume,
            ])


def main() -> None:

    sample_id = 0

    for pattern in PatternType:

        print(f"Generating {pattern.value}...")

        for _ in range(NUM_SAMPLES_PER_CLASS):
            save_sample(
                sample_id=sample_id,
                pattern=pattern,
            )

            sample_id += 1

    print("Dataset generation complete.")


if __name__ == "__main__":
    main()