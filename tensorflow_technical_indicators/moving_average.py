import tensorflow as tf


@tf.function
def simple_moving_average(candles, window_size, trim_window=True):

    moving_average = tf.TensorArray(tf.float32, candles.shape[0])

    for i in tf.range(start=0, limit=window_size-1):
        moving_average = moving_average.write(i, candles[i])

    for i in tf.range(start=window_size-1, limit=candles.shape[0]):
        window = candles[i-1:i+window_size-1]
        ma = tf.reduce_sum(window) / window_size
        moving_average = moving_average.write(i, [ma])

    ret = moving_average.stack()
    if trim_window:
        return ret[window_size-1:]

    return ret
