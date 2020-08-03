import tensorflow as tf
from .moving_average import simple_moving_average, exponential_moving_average


@tf.function
def upday(series):
    padded_series = tf.concat(
        [tf.zeros((1, series.shape[1])), series], axis=0)

    series_prev = padded_series[:-1]
    return tf.maximum(series - series_prev, tf.zeros(series.shape))


@ tf.function
def downday(series):
    padded_series = tf.concat(
        [tf.zeros((1, series.shape[1])), series], axis=0)

    series_prev = padded_series[:-1]
    return tf.maximum(series_prev - series, tf.zeros(series.shape))


@ tf.function
def rsi(series, time_window=7, method='sma'):
    up = upday(series)
    down = downday(series)

    maup = simple_moving_average(
        up, time_window) if method == 'sma' else exponential_moving_average(up, time_window)
    madown = simple_moving_average(
        down, time_window) if method == 'sma' else exponential_moving_average(down, time_window)

    rs = maup / madown

    return 100 - 100 / (1 + rs)
