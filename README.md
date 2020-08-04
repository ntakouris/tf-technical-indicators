# tensorflow-technical-indicators

Technical Indicators as TF Graph Functions!

    - Compatible with the rest of the tensorflow ecosystem
    - Super fast as tensorflow graph code

`pip install tensorflow-technical-indicators`

[![PyPI version](https://badge.fury.io/py/tensorflow-technical-indicators.svg)](https://badge.fury.io/py/fluent-tfx)

![Tests](https://github.com/ntakouris/tf-technical-indicators/workflows/Test%20Python%20Package/badge.svg)

(Coverage % is bad because tf graphs are not traced, only the `@tf.function`)
[![codecov](https://codecov.io/gh/ntakouris/tf-technical-indicators/branch/master/graph/badge.svg)](https://codecov.io/gh/ntakouris/tf-technical-indicators)

## Usage

```python

import tensorflow_technical_indicators as tfti

# assuming your tensors have dimensions: (time step, features[ohlcv])
# where candles[:, 0] is open, candles[:, 1] high, etc..

candles = [...]
# you can get
c = tfti.features.close(candles)
rsi = tfti.rsi(candles=c, window_size=7, method='ema')

# you can also pass multidimensional tensors with (time step, features)
# where features = open, close
# to calculate some indicator for both open and close
result = tfti.indicator(candles, ..params..)

# in general
# tfti.<indicator>(parameters)
# check the list below to find indicator names

```

## List of Indicators

```python
from tensorflow_technical_indicators import <indicator>
```

| Indicator                 | Implementation               |
| :------------------------ | :--------------------------- |
| SMA                       | `simple_moving_average`      |
| EMA                       | `exponential_moving_average` |
| RSI                       | `rsi`                        |
| MACD                      | `macd`                       |
| Stochastic Oscillator     |                              |
| Bolliger Bands            |                              |
| Fibonacci Retractment     |                              |
| Ichimoku Cloud            |                              |
| Standard Deviation        |                              |
| Average Directional Index |                              |
| More                      | To Come                      |

Need more indicators? Open up a pull request or open an issue :).
