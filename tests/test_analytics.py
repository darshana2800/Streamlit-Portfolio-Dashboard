import pandas as pd, numpy as np
import pytest
from src.prices import get_price_panel
from src.analytics import reconstruct_pos, portfolio_value, twr, annualized_volatility, max_drawdown

def test_reconstruct_pos_multitrade_same_day(trades_multi_day_one_ticker):
    pos = reconstruct_pos(trades_multi_day_one_ticker)
    aapl = pos["AAPL"]
    assert list(aapl) == [5, 6, 7]  # cumulative shares after each trade date

def test_portfolio_value_matches_shares_times_price(trades_multi_day_one_ticker):
    pos = reconstruct_pos(trades_multi_day_one_ticker)
    start = pos.index.min().strftime("%Y-%m-%d")
    end = (pos.index.max() + pd.Timedelta(days=5)).strftime("%Y-%m-%d")
    px = get_price_panel(["AAPL"], start, end).reindex(pos.index).ffill()
    val = portfolio_value(pos, px)
    assert np.isfinite(val.iloc[-1])
    assert pytest.approx(val.iloc[-1], rel=1e-6) == pos.iloc[-1, 0] * px.iloc[-1, 0]


def test_kpis_increasing_equity():
    s =  pd.Series([100.0, 110.0, 121.0], index=pd.date_range("2024-01-01", periods=3))
    assert twr(s) == pytest.approx(0.21, rel=1e-6)
    assert np.isfinite(annualized_volatility(s))
    assert max_drawdown(s) <= 0.0

def test_kpis_single_point_series():
    s = pd.Series([100.0], index=pd.date_range("2024-01-01", periods=1))
    assert twr(s) == 0.0
    assert np.isnan(annualized_volatility(s)) or annualized_volatility == 0.0
    assert max_drawdown(s) == 0.0                 