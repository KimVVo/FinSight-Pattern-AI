from .ohlcv import Candle
from enum import Enum

def create_bullish_engulfing(
    previous_close: float,
) -> list[Candle]:
    """
    Create two candles forming a bullish engulfing pattern.
    """

    # First candle: bearish
    first_open = previous_close
    first_close = previous_close * 0.97

    first_high = first_open * 1.005
    first_low = first_close * 0.995

    first = Candle(
        open=round(first_open, 2),
        high=round(first_high, 2),
        low=round(first_low, 2),
        close=round(first_close, 2),
        volume=1_000_000,
    )

    # Second candle: bullish and engulfs first candle's body
    second_open = first_close * 0.995
    second_close = first_open * 1.015

    second_high = second_close * 1.005
    second_low = second_open * 0.995

    second = Candle(
        open=round(second_open, 2),
        high=round(second_high, 2),
        low=round(second_low, 2),
        close=round(second_close, 2),
        volume=1_500_000,
    )

    return [first, second]


def create_bearish_engulfing(
    previous_close: float,
) -> list[Candle]:
    """
    Create two candles forming a bearish engulfing pattern.
    """

    # First candle: bullish
    first_open = previous_close
    first_close = previous_close * 1.03

    first_high = first_close * 1.005
    first_low = first_open * 0.995

    first = Candle(
        open=round(first_open, 2),
        high=round(first_high, 2),
        low=round(first_low, 2),
        close=round(first_close, 2),
        volume=1_000_000,
    )

    # Second candle: bearish and engulfs first candle's body
    second_open = first_close * 1.005
    second_close = first_open * 0.985

    second_high = second_open * 1.005
    second_low = second_close * 0.995

    second = Candle(
        open=round(second_open, 2),
        high=round(second_high, 2),
        low=round(second_low, 2),
        close=round(second_close, 2),
        volume=1_500_000,
    )

    return [first, second]


def create_doji(
    previous_close: float,
) -> list[Candle]:
    """
    Create a doji candle.
    """

    open_price = previous_close

    # Open and close are almost identical
    close_price = open_price * 1.0001

    high_price = open_price * 1.02
    low_price = open_price * 0.98

    doji = Candle(
        open=round(open_price, 2),
        high=round(high_price, 2),
        low=round(low_price, 2),
        close=round(close_price, 2),
        volume=1_000_000,
    )

    return [doji]


class PatternType(str, Enum):
    BULLISH_ENGULFING = "bullish_engulfing"
    BEARISH_ENGULFING = "bearish_engulfing"
    DOJI = "doji"
    NO_PATTERN = "no_pattern"