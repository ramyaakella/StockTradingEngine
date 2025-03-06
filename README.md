# StockTradingEngine
##Stock Trading Order Matching System

This is a simple stock trading order matching system implemented in Python using a list-of-lists approach for storing buy and sell orders. It supports multi-threaded order processing and matches trades based on price and availability.

###Features

Supports 1,024 different stock tickers.

Handles both Buy and Sell orders.

Orders are sorted and matched based on price.

Uses threading to simulate real-time trading.

###How It Works

Orders are added to buy or sell lists based on the ticker symbol.

Buy orders are sorted in descending order (highest price first).

Sell orders are sorted in ascending order (lowest price first).

The system continuously matches buy and sell orders based on price.

If a match occurs, the trade is executed, and quantities are updated.

###Installation

No external dependencies are required. Just ensure you have Python installed.

###Running the Program

Simply run the script:
```
python tradeEngine.py
```

This will start the simulation of trading orders.

Example Output
```
Matched 50 shares of STK1 at $100.5
Matched 30 shares of STK2 at $250.0
```

This output indicates that trades were successfully matched and executed.
