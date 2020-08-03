import tensorflow as tf


@tf.function
def _get_col(candles, idx):
    return candles[:, idx]


@tf.function
def open(candles):
    return _get_col(candles, 0)


@tf.function
def high(candles):
    return _get_col(candles, 1)


@tf.function
def low(candles):
    return _get_col(candles, 2)


@tf.function
def close(candles):
    return _get_col(candles, 3)


@tf.function
def volume(candles):
    return _get_col(candles, 4)
