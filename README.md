# Stock Market Simulation and Trading Strategy

This repository contains a simple implementation of a stock market simulation with a trading strategy based on stock price fluctuations. The goal is to simulate stock price updates, generate trading signals, and test a basic trading strategy.

## Features

### Stock Class

The `Stock` class represents a stock and includes:
- **Attributes**:
  - `name`: The name of the stock (e.g., "Apple").
  - `symbol`: The stock symbol (e.g., "AAPL").
  - `price`: The current price of the stock.
- **Methods**:
  - `updatePrice()`: Randomly updates the stock price at regular intervals to simulate price fluctuations in the market.

### Functions

1. **createStocks(num_stocks)**: Creates `num_stocks` instances of the `Stock` class with random names, symbols, and initial prices.
2. **displayStockMarket(stocks)**: Displays the current prices of all stocks in the market.
3. **buySignal(stock)**: Returns `True` if the stock's price has increased by a certain percentage since the last update, indicating a buy signal.
4. **sellSignal(stock)**: Returns `True` if the stock's price has decreased by a certain percentage since the last update, indicating a sell signal.
5. **testTradingStrategy(stocks, initial_balance, num_days)**: Simulates trading for the specified number of days using buy and sell signals. Tracks the portfolio and balance throughout the simulation and outputs the final results.

## Installation

To get started, clone this repository and navigate to the project folder.

```bash
