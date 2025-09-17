import pandas as pd
from src.prices import get_prices, get_price_panel


def test_get_prices():
    # Test fetching prices for a known ticker and date range
    ticker = "AAPL"
    start = "2024-02-20"
    end = "2024-03-15"
    prices = get_prices(ticker, start, end)
    
    assert isinstance(prices, pd.Series)
    assert not prices.empty
    assert prices.name == ticker
    assert prices.index.min() >= pd.to_datetime(start)
    assert prices.index.max() <= pd.to_datetime(end)
    assert prices.notna().any()

def test_get_price_panel_one_ticker():
    # Test fetching prices for a single ticker
    start = "2024-02-20"
    end = "2024-03-15"
    panel = get_price_panel(tickers=["AAPL"], start=start, end=end)
    assert isinstance(panel, pd.DataFrame)
    assert not panel.empty
    assert list(panel.columns) == ["AAPL"]
    assert panel.notna().any().all() # At least one non-NaN value

def test_get_price_panel_multiple_tickers_drop_bad():
    # Test fetching prices for multiple tickers
    start = "2024-02-20"
    end = "2024-03-15"
    tickers = ["AAPL", "MSFT", "BAD"]
    panel = get_price_panel(tickers=tickers, start=start, end=end)
    
    assert isinstance(panel, pd.DataFrame)
    assert not panel.empty
    assert set(panel.columns) == set(tickers) - {"BAD"}
    assert "BAD" not in panel.columns
    assert panel.notna().all().all()

