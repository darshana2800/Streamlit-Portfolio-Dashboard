# Streamlit Portfolio Dashboard

A Streamlit web app to visualize and analyze portfolio performance. Includes unit tests and a modular Python package.

## Features

- Interactive dashboard built with Streamlit
- Upload and analyze trade/portfolio data
- Visualize prices, returns, and analytics
- Unit tests for core functionality (pytest)

- **Input**  
  - A CSV of trades with columns like `date`, `ticker`, `side`, `qty`, and `price`.

- **Data Source**  
  - Prices are fetched automatically from Yahoo Finance using the `yfinance` API.

- **Processing**  
  - Reconstructs daily share positions per ticker from your trades.
  - Aligns prices to your trading dates and fills gaps for weekends and holidays.
  - Computes your total portfolio value over time.

- **Output**  
  - Displays key metrics including:
    - **Total Value**
    - **Time-Weighted Return (TWR)**
    - **Annualized Volatility**
    - **Maximum Drawdown**


## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/darshana2800/Streamlit-Portfolio-Dashboard.git
cd Streamlit-Portfolio-Dashboard
pip install -r requirements.txt
```


## Running the App

```bash
streamlit run home.py
```