from tensorflow_technical_indicators.features import open, high, low, close, volume
import tensorflow as tf


class FeaturesTest(tf.test.TestCase):

    def setUp(self):
        super(FeaturesTest, self).setUp()

    def testOHLCVColumnGettersWork(self):

        # Arrange
        candles = tf.constant([
            [0, 1, 2, 3, 4],  # open
            [0, 1, 2, 3, 4],  # high
            [0, 1, 2, 3, 4],  # low
            [0, 1, 2, 3, 4],  # close
            [0, 1, 2, 3, 4]  # volume
        ], dtype=tf.float32)

        # Act
        o = open(candles)
        h = high(candles)
        l = low(candles)
        c = close(candles)
        v = volume(candles)

        # Assert
        self.assertAllClose(o, tf.constant([0, 0, 0, 0, 0], dtype=tf.float32))
        self.assertAllClose(h, tf.constant([1, 1, 1, 1, 1], dtype=tf.float32))
        self.assertAllClose(l, tf.constant([2, 2, 2, 2, 2], dtype=tf.float32))
        self.assertAllClose(c, tf.constant([3, 3, 3, 3, 3], dtype=tf.float32))
        self.assertAllClose(v, tf.constant([4, 4, 4, 4, 4], dtype=tf.float32))


if __name__ == '__main__':
    tf.compat.v1.enable_v2_behavior()
    tf.test.main()
