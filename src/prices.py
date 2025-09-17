import pandas as pd, yfinance as yf
from functools import lru_cache

# Define cache for historical price data
@lru_cache(maxsize=256)
def get_prices(ticker: str, start:  str, end: str) -> pd.Series:
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    if df.empty: 
        # Return empty series if no data
        return pd.Series(dtype="float64", name=ticker)
    close = df["Close"]

    # If multiple columns (e.g., multi-index), take the first
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close.name = ticker
    return close

# Get the price of a stock on a specific date
def get_price_panel(tickers, start, end) -> pd.DataFrame:
    prices = [get_prices(t, start, end) for t in tickers]
    panel = pd.concat(prices, axis=1).sort_index()

    # Ensures panel is always a DataFrame
    if isinstance(panel, pd.Series):
        panel = panel.to_frame()

    # Drop columns with all NaN values
    panel = panel.loc[:, panel.notna().any()]
    return panel
