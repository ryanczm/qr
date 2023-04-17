# QR

This is a repo for quant analysis/data analysis projects in finance. I am still learning, so bear with me.

* `pairs_trading_nasdaq.ipynb` - This is a project with a writeup on my [website](https://ryan-chew.com/quant_pairs_trade.html), which details implementing, backtesting and evaluating (Sharpe and IR, etc) a low-frequency (biweekly) pairs trading strategy on chosen NASDAQ 100 equities pairs with 2018-2020 in-sample and 2021-present out-sample.
    * However, the main takeaway is that in-sample cointegration is generally a poor predictor of out-sample cointegration, and so another approach would be to research to identify features (e.g event based, macro based, etc) to predict lookahead cointegration of pairs, then trade cointegrated pairs.  
    * We also encounter several topics, like survivorship bias, multiple comparison bias, etc. The backtest is simplistic and does not account for market impact, which would be significant if we were to place larger orders.
    * Resources used were _Stefan Jansen's ML4T_, _Ernest Chan's QT_ and _Udacity/Worldquant's AI4T_.

* `uniswap_arb` - Technical project from Linden Shore for the Trading/Quant Analyst role.
    * Asked to simulate the behavior of the crypto dex Uniswap V2 or V3 protocol, calculate any arbitrage opportunity between imbalanced pools (and the optimal profit), then write tests to 1. check pool logic is correct 2. benchmark arbitrage calculation speed.
    * The optimal profit was calculated with convex optimization.
    * Everything was correct but the profit logic was slightly incorrect. I did this for the V2 protocol.

* `economic_regime_avm.ipynb` - Technical project from AVM Capital for the Quant Analyst Intern role. 
    * Asked to calculate returns of a quarterly rebalancing strategy of a portfolio of S&P, Gold & US Treasuries over several decades based on macro regimes (rising/falling growth/inflation from GDP/CPI data) and benchmark against long S&P performance. 
    * However, I was informed my strategy had lookahead bias, being unaware that the GDP/CPI figures were usually released after the start of the quarter. Thus, leading macro indicators (e.g PMI, yield curve spread, VIX) could be used instead.