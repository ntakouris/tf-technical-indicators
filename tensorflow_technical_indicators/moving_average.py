import tensorflow as tf
from features import CANDLES_INPUT_SIGNATURE


@tf.function(input_signature=CANDLES_INPUT_SIGNATURE)
def MovingAverage(candles):
    pass
