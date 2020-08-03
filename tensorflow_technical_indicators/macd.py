import tensorflow as tf
from .moving_average import simple_moving_average, exponential_moving_average


@tf.function
def macd(series, a=12, b=26, c=9):
    ema_a = exponential_moving_average(series, a)
    ema_b = exponential_moving_average(series, b)

    signal_line = exponential_moving_average(series, c)

    macd_line = ema_a - ema_b
    return macd_line - signal_line
