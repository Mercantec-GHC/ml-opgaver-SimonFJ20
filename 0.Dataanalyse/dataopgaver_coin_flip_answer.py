import random
from enum import Enum, auto
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CoinFlip(Enum):
    Heads = auto()
    Tails = auto()

def coin_flip() -> CoinFlip:
    if random.random() < 0.5:
        return CoinFlip.Heads
    else:
        return CoinFlip.Tails

runs = [coin_flip() for _ in range(0, 100_000)]
heads_amount = len([run for run in runs if run == CoinFlip.Heads])
print("heads:", heads_amount)
tails_amount = len([run for run in runs if run == CoinFlip.Tails])
print("tails:", tails_amount)
print("heads%:", heads_amount / len(runs))

def percentage_over_time(runs: list[CoinFlip]):
    result = []
    heads_amount = 0
    for i, run in enumerate(runs):
        if run == CoinFlip.Heads:
            heads_amount += 1
        average = heads_amount / (i + 1)
        result.append(average)
    return result
    
data = percentage_over_time(runs)


plt.figure(figsize=(12, 8))
plt.plot(data)
plt.ylim([0, 1])
plt.show()

