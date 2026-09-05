from dataclasses import dataclass
import random


@dataclass
class Candle:
    open: float
    high: float
    low: float
    close: float
    volume: int


def generate_random_candle(
    previous_close: float,
    trend: float = 0.0,
    volatility: float = 0.02,
) -> Candle:
    """
    Generate one synthetic OHLCV candle.

    Args:
        previous_close: Previous candle's closing price.
        trend: Directional bias. Positive = bullish, negative = bearish.
        volatility: Controls the size of price movements.

    Returns:
        A synthetic Candle.
    """

    # Random price movement
    change = random.gauss(trend, volatility)

    open_price = previous_close

    close_price = open_price * (1 + change)

    # Ensure positive prices
    close_price = max(close_price, 0.01)

    # Generate wick sizes
    upper_wick = random.uniform(0.001, volatility)
    lower_wick = random.uniform(0.001, volatility)

    high_price = max(open_price, close_price) * (1 + upper_wick)
    low_price = min(open_price, close_price) * (1 - lower_wick)

    # Synthetic trading volume
    volume = random.randint(500_000, 5_000_000)

    return Candle(
        open=round(open_price, 2),
        high=round(high_price, 2),
        low=round(low_price, 2),
        close=round(close_price, 2),
        volume=volume,
    )


def generate_market_sequence(
    num_candles: int = 50,
    starting_price: float = 100.0,
) -> list[Candle]:
    """
    Generate a sequence of synthetic market candles.
    """

    candles: list[Candle] = []

    current_price = starting_price

    # Randomly choose an overall market environment
    trend = random.choice([
        -0.001,
        0.0,
        0.001,
    ])

    volatility = random.uniform(0.01, 0.03)

    for _ in range(num_candles):
        candle = generate_random_candle(
            previous_close=current_price,
            trend=trend,
            volatility=volatility,
        )

        candles.append(candle)
        current_price = candle.close

    return candles