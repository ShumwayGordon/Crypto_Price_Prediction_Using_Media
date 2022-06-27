import datetime
from pathlib import Path
from tqdm import tqdm

import pandas as pd

import yfinance as yf


def main():
    data_dir = Path("currencies")
    coins = pd.read_csv(data_dir / "coins.csv")
    for coin in tqdm(coins.Coin):
        df = yf.Ticker(coin).history(start="2010-01-01",  end=datetime.datetime.now())
        df.to_csv(data_dir / f"{coin}.csv")
    

if __name__ == "__main__":
    main()