import random
import threading
import time

class Order: 
    def __init__(self, OrderType, TickerSymbol, Quantity, Price):
        self.order_type = OrderType  
        self.ticker = TickerSymbol
        self.quantity = Quantity
        self.price = Price

class Stock_trades:
    def __init__(self):

        self.buyTrades = [[] for _ in range(1024)]
        self.sellTrades = [[] for _ in range(1024)]
        self.lock = threading.Lock()

    def _ticker_index(self, TickerSymbol):

        return int(TickerSymbol[3:]) - 1

    def addOrder(self, OrderType, TickerSymbol, Quantity, Price):
        order = Order(OrderType, TickerSymbol, Quantity, Price)
        ticker_index = self._ticker_index(TickerSymbol)

        with self.lock:

            if OrderType == "Buy":
                orders = self.buyTrades[ticker_index]
                index = 0
                while index < len(orders) and orders[index].price >= order.price:
                    index += 1
                orders.insert(index, order)

            elif OrderType == "Sell":
                orders = self.sellTrades[ticker_index]
                index = 0
                while index < len(orders) and orders[index].price <= order.price:
                    index += 1
                orders.insert(index, order)

            else:
                raise Exception("Invalid Order Type")

    def matchOrder(self):
        with self.lock:
            for ticker_index in range(1024):
                buy_orders = self.buyTrades[ticker_index]
                sell_orders = self.sellTrades[ticker_index]

                i, j = 0, 0
                new_buy_orders = []
                new_sell_orders = []

                while i < len(buy_orders) and j < len(sell_orders):
                    buy_order = buy_orders[i]
                    sell_order = sell_orders[j]

                    if buy_order.price >= sell_order.price:
                        trade_quantity = min(buy_order.quantity, sell_order.quantity)
                        if trade_quantity > 0:
                            buy_order.quantity -= trade_quantity
                            sell_order.quantity -= trade_quantity
                            print(f"Matched {trade_quantity} shares of STK{ticker_index+1} at ${sell_order.price}")

                        if buy_order.quantity == 0:
                            i += 1
                        else:
                            new_buy_orders.append(buy_order)
                            i += 1  

                        if sell_order.quantity == 0:
                            j += 1
                        else:
                            new_sell_orders.append(sell_order)
                            j += 1  
                    else:
                       
                        break

              
                new_buy_orders.extend(buy_orders[i:])
                new_sell_orders.extend(sell_orders[j:])

               
                self.buyTrades[ticker_index] = [order for order in new_buy_orders if order.quantity > 0]
                self.sellTrades[ticker_index] = [order for order in new_sell_orders if order.quantity > 0]

def simulate_trading(stock_trades):
    tickers = [f"STK{i}" for i in range(1, 1025)]
    while True:
        order_type = random.choice(["Buy", "Sell"])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)

        stock_trades.addOrder(order_type, ticker, quantity, price)
        stock_trades.matchOrder() 

        time.sleep(random.uniform(0.1, 0.5))  

if __name__ == "__main__":
    stock_trades = Stock_trades()
    trading_thread = threading.Thread(target=simulate_trading, args=(stock_trades,))
    trading_thread.start()
