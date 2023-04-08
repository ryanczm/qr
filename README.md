# QR

This is a repo for quant analysis/data analysis projects in finance. I am still learning, so bear with me.

* `pairs_trading_nasdaq.ipynb` - This is a project with a writeup on my [website](https://ryan-chew.com/quant_pairs_trade.html), which details implementing, backtesting and evaluating (Sharpe and IR, etc) a pairs trading strategy on NASDAQ 100 equities. However, the main takeaway is that in-sample cointegration is generally a poor predictor of out-sample cointegration, and so another approach would be to research to identify features (e.g event based, macro based, etc) to predict lookahead cointegration of pairs, then trade cointegrated pairs.  We also encounter several topics, like survivorship bias, multiple comparison bias, etc. The backtest is simplistic and does not account for market impact and transaction costs. Resources used were _Stefan Jansen's ML4T_, _Ernest Chan's QT_ and _Udacity/Worldquant's AI4T_.

* `uniswap_arb` - Lorem Ipsum

* `economic_regime_avm.ipynb` - Lorem Ipsum. 