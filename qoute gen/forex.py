import pandas as pd
import numpy as np
import requests
import json
import time

# Simulated historical forex data
# Replace this with actual data retrieval from a forex API or database
historical_data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='B'),
    'EURUSD': np.random.uniform(low=1.0, high=1.2, size=(260,))
}
df = pd.DataFrame(historical_data)
df.set_index('Date', inplace=True)

def analyze_forex_data(df):
    # Calculate moving averages
    df['SMA_50'] = df['EURUSD'].rolling(window=50).mean()
    df['SMA_200'] = df['EURUSD'].rolling(window=200).mean()

    # Determine trading signals based on moving averages
    df['Signal'] = np.where(df['SMA_50'] > df['SMA_200'], 'BUY', 'SELL')

    return df

def calculate_position_size(account_balance, risk_per_trade, stop_loss):
    # Calculate position size based on risk per trade and stop loss percentage
    position_size = (account_balance * risk_per_trade) / stop_loss
    return position_size

def execute_trade(trade_signal, position_size):
    # Simulated execution of trade
    # Replace this with actual execution through broker API
    print(f"Executing {trade_signal} trade with position size: {position_size}")

def fetch_live_forex_data(symbol):
    # Simulated function to fetch live forex data from an API
    # Replace this with actual API integration
    url = f"https://api.example.com/forex/{symbol}/live"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['price']
    else:
        raise Exception(f"Error fetching live data for {symbol}")

if __name__ == "__main__":
    # Con
    account_balance = 10000  
    risk_per_trade = 0.02  
    stop_loss = 0.01  

    
    while True:
        live_price = fetch_live_forex_data('EURUSD')
        current_data = pd.DataFrame({'Date': [pd.Timestamp.now()], 'EURUSD': [live_price]})
        current_data.set_index('Date', inplace=True)
        df = pd.concat([df, current_data])

        analyzed_data = analyze_forex_data(df)
        last_row = analyzed_data.iloc[-1]
        trade_signal = last_row['Signal']

        if trade_signal:
            position_size = calculate_position_size(account_balance, risk_per_trade, stop_loss)
            execute_trade(trade_signal, position_size)
        
        time.sleep(60)  # Simulate checking every minute for new signals
