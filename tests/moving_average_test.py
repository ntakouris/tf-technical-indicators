from tensorflow_technical_indicators.features import open, high, low, close, volume
from tensorflow_technical_indicators.moving_average import simple_moving_average

import tensorflow as tf


class MovingAverageTest(tf.test.TestCase):

    def setUp(self):
        super(MovingAverageTest, self).setUp()

    def testSimpleMovingAverageWorksNoTrim(self):

        # Arrange
        candles = tf.constant([
            [5],
            [10],
            [15],
            [25]
        ], dtype=tf.float32)

        # Act
        sma = simple_moving_average(
            candles=candles, window_size=2, trim_window=False)

        # Assert
        expected = tf.reshape(tf.constant(
            [5, 7.5, 12.5, 20], dtype=tf.float32), shape=(4, 1))
        self.assertAllClose(sma, expected)

    def testSimpleMovingAverageWorksWithTrim(self):

        # Arrange
        candles = tf.constant([
            [5],
            [10],
            [15],
            [25]
        ], dtype=tf.float32)

        # Act
        sma = simple_moving_average(
            candles=candles, window_size=2, trim_window=True)

        # Assert
        expected = tf.reshape(tf.constant(
            [7.5, 12.5, 20], dtype=tf.float32), shape=(3, 1))
        self.assertAllClose(sma, expected)


if __name__ == '__main__':
    tf.compat.v1.enable_v2_behavior()
    tf.test.main()
