from tensorflow_technical_indicators.features import open, high, low, close, volume
from tensorflow_technical_indicators.moving_average import simple_moving_average, exponential_moving_average

import tensorflow as tf


class MovingAverageTest(tf.test.TestCase):

    def setUp(self):
        super(MovingAverageTest, self).setUp()

    def testSimpleMovingAverageWorksOneDim(self):

        # Arrange
        candles = tf.constant([
            [5],
            [10],
            [15],
            [25]
        ], dtype=tf.float32)

        # Act
        sma = simple_moving_average(
            candles=candles, window_size=2)

        # Assert
        expected = tf.constant([
            [5],
            [7.5],
            [12.5],
            [20]])
        self.assertAllClose(sma, expected)

    def testSimpleMovingAverageWorksManyDims(self):

        # Arrange
        candles = tf.constant([
            [5, 5],
            [10, 15],
            [15, 20],
            [25, 30]
        ], dtype=tf.float32)

        # Act
        sma = simple_moving_average(
            candles=candles, window_size=2)

        # Assert
        expected = tf.constant([
            [5, 5],
            [7.5, 10],
            [12.5, 17.5],
            [20, 25]])
        self.assertAllClose(sma, expected)

    def testExponentialMovingAverageWorksOneDim(self):

        # Arrange
        candles = tf.constant([
            [2.0],
            [4.0],
            [6.0],
            [8.0]
        ], dtype=tf.float32)

        # Act
        ema = exponential_moving_average(
            candles=candles, window_size=2)

        # Assert
        expected = tf.constant([
            [2],
            [3.66666],
            [5.22222],
            [7.074074]])
        self.assertAllClose(ema, expected, rtol=1e-04)

    def testExponentialMovingAverageWorksManyDims(self):

        # Arrange
        candles = tf.constant([
            [2.0, 2.0],
            [4.0, 4.0],
            [6.0, 6.0],
            [8.0, 8.0]
        ], dtype=tf.float32)

        # Act
        ema = exponential_moving_average(
            candles=candles, window_size=2)

        # Assert
        expected = tf.constant([
            [2, 2],
            [3.66666, 3.66666],
            [5.22222, 5.2222],
            [7.074074, 7.074074]])
        self.assertAllClose(ema, expected, rtol=1e-04)


if __name__ == '__main__':
    tf.compat.v1.enable_v2_behavior()
    tf.test.main()
