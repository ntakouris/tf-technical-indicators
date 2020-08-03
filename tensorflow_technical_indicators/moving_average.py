import tensorflow as tf


@tf.function
def simple_moving_average(candles, window_size=7):

    moving_average = tf.TensorArray(tf.float32, candles.shape[0])

    for i in tf.range(start=0, limit=window_size-1):
        moving_average = moving_average.write(i, candles[i])

    for i in tf.range(start=window_size-1, limit=candles.shape[0]):
        window = candles[i-1:i+window_size-1]
        ma = tf.reduce_sum(window, axis=0) / window_size
        moving_average = moving_average.write(i, ma)

    return moving_average.stack()


@tf.function
def exponential_moving_average(candles, window_size=9):
    moving_average = tf.TensorArray(tf.float32, candles.shape[0])

    initial_sma = tf.reduce_sum(candles[:window_size], axis=0) / window_size
    multiplier = 2 / (window_size + 1)

    moving_average = moving_average.write(window_size-2, initial_sma)

    for i in tf.range(start=window_size-1, limit=candles.shape[0]):
        prev_ema = moving_average.read(i-1)

        next_ema = (candles[i] * multiplier) + (prev_ema * (1 - multiplier))

        moving_average = moving_average.write(i, next_ema)

    for i in tf.range(start=0, limit=window_size-1):
        moving_average = moving_average.write(i, candles[i])

    return moving_average.stack()
