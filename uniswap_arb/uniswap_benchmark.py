import time
from scipy.optimize import minimize, Bounds
import numpy as np
import pandas as pd
from uniswap_arb import simulate_arb

def upper_bound(row):
    a, b = sum(row[:2]), sum(row[2:])
    total = a + b
    bound = b/total * abs(row[0] - row[1]) + a/total * abs(row[2] - row[3])
    return bound

def time_optimal_profit(ax, ay, bx, by):
    t1 = time.perf_counter()
    lower, upper = 1e-05, max(ay/ax, by/bx) * max(ax, bx)
    midpoint = upper/2
    res = minimize(simulate_arb, x0=midpoint, bounds=Bounds(lower,upper), args=(ax, ay, bx, by, -1))
    t2 = time.perf_counter()
    return pd.Series([t2 - t1, res.nit])

def time_distribution():
    dai_1 = np.random.uniform(7000000, 8000000, size=(100))
    eth_1 = np.random.uniform(3000, 5000, size=(100))
    dai_2 = np.random.uniform(7000000, 8000000, size=(100))
    eth_2 = np.random.uniform(3000, 5000, size=(100))
    pool_df = pd.DataFrame({"x1": dai_1, "y1": eth_1, "x2": dai_2, "y2": eth_2})
    pool_df[['time', 'iter']] = pool_df.apply(lambda row: time_optimal_profit(*row),axis=1)
    print(pool_df.time.describe())
    return pool_df.time.describe()

if __name__ == '__main__':
    time_distribution()