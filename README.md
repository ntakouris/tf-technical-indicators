# tf-technical-indicators

Technical Indicators as TF Graph Functions!

    - Compatible with the rest of the tensorflow ecosystem
    - Super fast as tensorflow graph code

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

`from tensorflow_technical_indicators import <indicator>`

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
