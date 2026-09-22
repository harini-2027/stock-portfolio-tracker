#stores the available stocks and their current unit prices
stock_prices = {
    'AAPL': 180.00,
    'TSLA': 250.00,
    'GOOGL': 140.00,
    'AMZN': 175.00
}
#dictionary to store the user's selected stocks and quantities
portfolio = {}
total_investment = 0.0
print("welcome to stock portfolio tracker")
#display the stocks available in the database
print(f"Available assets for tracking: {', '.join(stock_prices.keys())}\n")
#take stock symbols and quantities from the user until they choose to finsih
while True:
    symbol = input("enter stock symbol(or type 'done' to finish):").upper().strip()
    if symbol == 'DONE':
        break
#checking weather the entered stock exists in our database
    if symbol not in stock_prices:
        print(f"{symbol}not in our database, please select from {list(stock_prices.keys())}")
        continue
    try:
        quantity = float(input(f"Enter quantity of shares for {symbol}: "))
        if quantity <= 0:
            print("quality must be greater than zero.")
            continue
#add the quantity to the portfolio
        portfolio[symbol] = portfolio.get(symbol, 0.0) + quantity
        print(f"✅ Added {quantity} shares of {symbol} to tracking.")
    except ValueError:
        print("❌ Invalid input! Please enter a valid numerical value for quantity.")
#calculate and display the value of each stock holding
print("\n current portfolio summary")
print("=" *45)
print(f"{'Stock':<10} {'Quantity':<12} {'Unit Price':<12} {'Total Value':<11}")
print("-" * 45)
for stock,qty in portfolio.items():   
    unit_price = stock_prices[stock]
    holding_value = qty * unit_price
    total_investment += holding_value
print(f"{stock:<10} {qty:<12.2f} ₹{unit_price:<11.2f} ₹{holding_value:<10.2f}")       
print("=" * 45)
print(f" Total Estimated Portfolio Value: ₹{total_investment:,.2f}\n")   
#export portfolio details as the text file   
if portfolio:
    save_file = input("would you like to export the data?(text/csv/no):").lower().strip()
    if save_file == "txt":
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("PORTFOLIO TRACKER REPORT\n")
            file.write("=" * 40 + "\n")
            for stock, qty in portfolio.items():
                file.write(f"Asset: {stock} | Shares: {qty:.2f} | Market Price: ₹{stock_prices[stock]:.2f}\n")
            file.write("=" * 40 + "\n")
            file.write(f"Total Portfolio Valuation: ₹{total_investment:,.2f}\n")
        print("💾 Success! Report compiled inside 'portfolio_report.txt'")
#export portfolio details as a csv files
    elif save_file == 'csv':
        with open("portfolio_report.csv", "w", encoding="utf-8") as file:
            file.write("Ticker,Quantity,UnitPrice,TotalValue\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
            file.write(f"TOTAL,,, {total_investment}\n")
        print("💾 Success! Spreadsheet generated inside 'portfolio_report.csv'")
else:
    print("No assets added. Tracker shutting down.")



