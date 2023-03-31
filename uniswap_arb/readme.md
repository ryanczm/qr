# Writeup (Readme)

* `uniswap_arb.py` - Main logic and code
* `uniswap_arbitrage.ipynb` - Jupyter notebook for analysis
* `uniswap_tests.py` - Test cases for swap method
* `uniswap_benchmark.py` - Benchmark for arbitrage calculation

## Main Code

The class `UniswapPool` implements the Uniswap V2 pool logic, with the `add_liquidity`, `remove_liquidity` and `swap` methods. This is then used by the `eth_in, eth_profit = optimal profit(ax, ay, bx, by)` function, which for given $X_1, Y_1, X_1, Y_2$ calculates the maximum profit that can be made and the initial ETH amount to swap in. The pool values were referenced from this [v2 pool](https://v2.info.uniswap.org/pair/0xa478c2975ab1ea89e8196811f51a7b7ade33eb11).

`python -m uniswap_arb.py`

Prompts with "Randomize Inputs? [y/n]"? If `n`, prompts you to enter input values.

```
Randomize inputs? [y/n]: n
Enter DAI in pool A (X1): 7400000
Enter ETH in pool A (Y1): 5000
Enter DAI in pool B (X2): 7500000
Enter ETH in pool B (Y2): 4000
ETH in: 243.79791307173326 | ETH profit: 29.792787666814377
Buy DAI in pool B with 243.79791307173326 ETH and sell it in pool A for a profit of 29.792787666814377
```
If  `y`, then samples `x1, x2` randomly from $\sim U(7000000, 8000000)$ and `y1`, `y2` from $\sim U(3000,5000)$. This range is too wide to be unrealistic but I don't trade crypto so I don't know a realistic range.

```
Randomize inputs? [y/n]: y
Randomly generated values: X1: 7234883.461266833, Y1: 3361.4715525543306, X2: 7996086.567745868, Y2:4590.632046006774
ETH in: 191.87043779523333 | ETH profit: 20.776935384189755
Buy DAI in pool A with 191.87043779523333 ETH and sell it in pool B for a profit of 20.776935384189755
```


## Arbitrage Calculation Logic

The profit function, given constants $X_1, Y_1, X_2, Y_2$, fee constant $\gamma=0.997$ and $k_i = X_i * Y_i$ and initial ETH input $y'$ can be written as: $$P(y')=Y_2 - \frac{k_2}{X_2 + \gamma[X_1 - \frac{k_1}{Y_1 + \gamma \cdot y' }]} - y'$$ Which simulates swapping ETH to DAI in the pool where DAI is cheaper, then selling that DAI for ETH in the pool where DAI is more expensive. We could set the derivative $\frac{dP}{dy'}=0$ and solve for $y'$. However, optimization was chosen as the function is convex & single-variable and analytically solving for the maximum of the function is troublesome. To find optimal `y'` for the given `X_i, Y_i`, we use `scipy.optimize.minimize` to optimize the profit function with bounds. The lower bound is near 0, while I chose the upper bound by the formula $$B_u =\max(\frac{y_1}{x_1}, \frac{y_2}{x_2}) * \max(x_1,x_2)$$ which was empirically chosen to get a small bound while covering the maximum profit. and the initial guess `x0` is midpoint of these bounds. However, there seems to be a better method for choosing an upper bound as this bound is overkill for imbalanced ratios (e.g 7,737,000 DAI to 4300 ETH).If speed is a concern, solving the analytical formula would be quicker. It is in the form $P=\frac{ax+b}{cx+d}$ which can be evaluated with the quotient rule to give $P'=\frac{ad-bc}{(cx+d)^2}$. However to manipulate the original expression into the fraction form is very troublesome.

To find a suitable upper bound, we can take the historical max/min values of DAI/ETH in the pool for a past period, then plug them into the optimization to see what ETH input is produced, and take that as the bound.

## Test Cases

Test cases were written to test the following.

* (In)valid ratio in adding/removing liquidity via `add_liquidity` and `remove_liquidity`
* (In)valid input token amounts (negative or zero tokens) in constructing the `UniswapPool` or in calling the `swap` function
* `k` always increasing after `swap` is called.
* Correct token name input "ETH" or "DAI" in `swap`.

`python -m uniswap_tests.py`

## Benchmark

Unfortunately, I couldn't figure out what this part (non-blocking) meant in the context of the problem in time and if it was related to multithreading/multiprocessing. However, I would be keen to understand why it is necessary to have a non-blocking calculation and what it entails in this context.

However, the benchmark file will simulate running the arbitrage logic 100 times with randomly generated values of tokens in either pool (dispersed around 7,400,000 for DAI and 4300 for ETH from this [pool](https://v2.info.uniswap.org/pair/0xa478c2975ab1ea89e8196811f51a7b7ade33eb11) ), and prints the quartiles of the distribution of time taken in seconds, the average time taken is 0.05s. Of course, this is not indicative of actual time as the optimization bound could be reduced for faster calculation times.
 
`python -m uniswap_benchmark.py`
```
count    100.000000
mean       0.051802
std        0.033203
min        0.006791
25%        0.026293
50%        0.042849
75%        0.065217
max        0.180395
Name: time, dtype: float64
```




