from tensorflow_technical_indicators.rsi import rsi, upday, downday

import tensorflow as tf


class RsiTest(tf.test.TestCase):

    def setUp(self):
        super(RsiTest, self).setUp()

    def testUpDayWorks(self):
        # Arrange
        series = tf.constant(
            [[1, 1], [2, 2], [1, 1], [5, 4]], dtype=tf.float32)

        # Act
        upd = upday(series)

        # Assert
        expected = tf.constant([[1, 1], [1, 1], [0, 0], [4, 3]])
        self.assertAllClose(upd, expected)

    def testDownDayWorks(self):
        # Arrange
        series = tf.constant(
            [[1, 3], [2, 2], [1, 1], [5, 5]], dtype=tf.float32)

        # Act
        dd = downday(series)

        # Assert
        expected = tf.constant([[0, 0], [0, 1], [1, 1], [0, 0]])
        self.assertAllClose(dd, expected)

    def testRsiWorks(self):
        # Arrange
        series = tf.constant(
            [[1], [2], [1], [5], [3], [6], [2]], dtype=tf.float32)

        # Act
        result = rsi(series, time_window=2)

        # Assert
        expected = tf.constant(
            [[100], [100], [50], [80], [66.6666], [60], [42.857143]])
        self.assertAllClose(result, expected, rtol=1e-02)

    def testRsiExponentialDoesNotCrash(self):
        # Arrange
        series = tf.constant(
            [[1], [2], [1], [5], [3], [6], [2]], dtype=tf.float32)

        # Act
        rsi(series, time_window=2, method='ema')


if __name__ == '__main__':
    tf.compat.v1.enable_v2_behavior()
    tf.test.main()
