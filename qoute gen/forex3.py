import pandas as pd
import numpy as np
import requests
import json
import time
import yfinance as yf

# Replace with your actual API key
api_key = '35005b9b4e6d18cb9cb81be7'

def fetch_exchange_rate():
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']['EUR']
    else:
        return None

def fetch_historical_data(currency_pair, start_date, end_date):
    data = yf.download(currency_pair, start=start_date, end=end_date)
    return data

def analyze_forex_data(df):
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    df['Signal'] = np.where(df['SMA_50'] > df['SMA_200'], 'BUY', 'SELL')
    return df

def calculate_position_size(account_balance, risk_per_trade, stop_loss):
    position_size = (account_balance * risk_per_trade) / stop_loss
    return position_size

def execute_trade(trade_signal, position_size):
    print(f"Executing {trade_signal} trade with position size: {position_size}")

def fetch_live_forex_data(symbol):
    url = f"(https://v6.exchangerate-api.com/v6/{api_key}/latest/USD')"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['conversion_rates'][symbol]
    else:
        raise Exception(f"Error fetching live data for {symbol}")

def main():
    account_balance = 10000
    risk_per_trade = 0.02
    stop_loss = 0.01
    buy_signal_threshold = 1.005
    sell_signal_threshold = 0.995
    currency_pair = 'EURUSD'
    
    historical_data = fetch_historical_data(currency_pair, '2020-01-01', '2023-12-31')
    historical_data['Date'] = pd.to_datetime(historical_data.index)
    historical_data.set_index('Date', inplace=True)
    
    while True:
        live_price = fetch_live_forex_data('EUR')
        current_data = pd.DataFrame({'Date': [pd.Timestamp.now()], 'Close': [live_price]})
        current_data.set_index('Date', inplace=True)
        historical_data = pd.concat([historical_data, current_data])
        analyzed_data = analyze_forex_data(historical_data)
        last_row = analyzed_data.iloc[-1]
        trade_signal = last_row['Signal']
        
        if trade_signal:
            position_size = calculate_position_size(account_balance, risk_per_trade, stop_loss)
            execute_trade(trade_signal, position_size)
        
        if live_price > (historical_data['Close'].iloc[-2] * buy_signal_threshold):
            signal = 'buy'
        elif live_price < (historical_data['Close'].iloc[-2] * sell_signal_threshold):
            signal = 'sell'
        else:
            signal = 'hold'
        print(f'signal:{signal}')
        
        if live_price > historical_data['Close'].iloc[-2]:
            rise_fall = 'rise'
        else:
            rise_fall = 'fall'
        print(f'rise/fall:{rise_fall}')
        
        exchange_rate = fetch_exchange_rate()
        print(f'EUR to USD exchange rate: {exchange_rate}')
        
        time.sleep(60)

if __name__ == "_main_":
    main() 