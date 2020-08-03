import tensorflow as tf

CANDLES_INPUT_SIGNATURE = [tf.TensorSpec(shape=(None, 5), dtype=tf.float32)]


@tf.function(input_signature=(CANDLES_INPUT_SIGNATURE[0], tf.TensorSpec(shape=(1), dtype=tf.int32)))
def _get_col(candles, idx):
    return candles[idx[0], :]


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def open(candles):
    return _get_col(candles, tf.constant([0]))


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def high(candles):
    return _get_col(candles, tf.constant([1]))


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def low(candles):
    return _get_col(candles, tf.constant([2]))


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def close(candles):
    return _get_col(candles, tf.constant([3]))


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def volume(candles):
    return _get_col(candles, tf.constant([4]))
