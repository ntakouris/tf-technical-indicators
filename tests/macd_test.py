from tensorflow_technical_indicators.macd import macd

import tensorflow as tf


class RsiTest(tf.test.TestCase):

    def setUp(self):
        super(RsiTest, self).setUp()

    def testMacdWorks(self):
        # Arrange
        series = tf.constant(
            [[1, 1], [2, 1], [1, 1], [4, 1], [5, 1], [5, 1], [9, 1]], dtype=tf.float32)

        # Act
        result = macd(series, a=2, b=4, c=2)

        # Assert
        expected = tf.constant(
            [[-1, -1], [-2, -1], [-1, -1], [-2.8, -1], [-3.68, -1], [-4.208, -1], [-6.124, -1]])
        self.assertAllClose(result, expected, rtol=1e-03)


if __name__ == '__main__':
    tf.compat.v1.enable_v2_behavior()
    tf.test.main()
