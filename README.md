
# BTC/USDT Moving Average Crossover Backtest

## Overview

This project implements a simple moving average (MA) crossover strategy on historical BTC/USDT price data to evaluate whether it outperforms a passive buy-and-hold investment.

The strategy is backtested on both **1-hour** and **4-hour** Binance candlestick datasets to compare how the same trading logic behaves across different market resolutions.

In addition to the backtest, the project includes:

* Performance comparison against Buy & Hold
* Risk metrics and performance evaluation
* Trade and P&L logging
* Event-driven notification simulation
* Performance visualizations

---

## Strategy
[I found this resource helpful](https://volity.io/forex/golden-cross-vs-death-cross/)
The strategy uses two Simple Moving Averages (SMA):

* **Fast Moving Average:** 20 periods
* **Slow Moving Average:** 50 periods

### Entry

A long position is opened when the fast moving average crosses **above** the slow moving average.

### Exit

The position is closed when the fast moving average crosses **below** the slow moving average.

Only one position can be open at a time, and no short selling or leverage is used.

---

## Assumptions

* Initial capital: **$10,000**
* Long-only strategy
* No leverage
* No transaction fees or slippage
* Orders are executed at the close of the signal candle
* Position size is 100% of available capital
* Risk-free rate assumed to be **0%** for Sharpe ratio calculations

---

## Project Outputs

The notebook generates:

* Moving average crossover signals
* Equity curve
* Buy & Hold benchmark
* Maximum drawdown
* Annualized Sharpe ratio
* Win rate
* Number of trades
* Trade log
* Notification log
* Performance comparison charts

---

## Notifications

The project includes a simulated event-driven notification system designed to resemble a production monitoring service (e.g. Slack).

Example notification events include:

* BUY_SIGNAL
* SELL_SIGNAL
* TRADE_COMPLETED
* DRAWDOWN_BREACH

Each notification includes a timestamp, event type, severity level, and descriptive message.

---

## Repository Structure

```text
.
├── notebook.ipynb
├── BTCUSDT_1h.csv
├── BTCUSDT_4h.csv
├── hourly_trade_log.csv
├── four_hour_trade_log.csv
├── hourly_notifications.csv
├── four_hour_notifications.csv
└── README.md
```

---

## Requirements

Install dependencies:

```bash
uv venv env
env\scripts\activate
uv pip install -r requirements.txt
```

---

## Running the Project

Open the notebook and execute all cells sequentially.

The notebook will:

1. Load the Binance datasets.
2. Calculate moving averages.
3. Generate trading signals.
4. Execute the backtest.
5. Compute performance metrics.
6. Generate charts.
7. Export trade logs and notification logs.
