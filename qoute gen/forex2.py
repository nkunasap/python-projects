import pandas as pd
import numpy as np
import requests
import json
import time
import yfinance as yf

historical_data = {  # type: ignore
    currency_pair = 'eurusd=x'  # type: ignore
    'Date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='B'), # type: ignore
    'EURUSD': np.random.uniform(low=1.0, high=1.2, size=(260,))
}
df = pd.DataFrame(historical_data)
df.set_index('Date', inplace=True)
data = yf.ticket(currency_pair) # type: ignore

def analyze_forex_data(df):
    
    df['SMA_50'] = df['EURUSD'].rolling(window=50).mean()
    df['SMA_200'] = df['EURUSD'].rolling(window=200).mean()

   
    df['Signal'] = np.where(df['SMA_50'] > df['SMA_200'], 'BUY', 'SELL')
    currency_price = data.info['regularmarketprice']
    

    return df

def calculate_position_size(account_balance, risk_per_trade, stop_loss):
    
    position_size = (account_balance * risk_per_trade) / stop_loss
    return position_size

def execute_trade(trade_signal, position_size):
   
    print(f"Executing {trade_signal} trade with position size: {position_size}")

def fetch_live_forex_data(symbol):
    data = yf.ticker(current_data) # type: ignore
    
    url = f"https://api.example.com/forex/{symbol}/live"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['price']
    else:
        raise Exception(f"Error fetching live data for {symbol}")

if __name__ == "__main__":
    
    account_balance = 10000  
    risk_per_trade = 0.02  
    stop_loss = 0.01  
     buy_signal_threshold=1.005 
     sell_signal_threshold=0.995
    
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
        
        if current_price > (data.info['previouscose']*buy_signal_threshold): # type: ignore
            signal = buy # type: ignore
        elif current_price <(data.info['previousclose']*sell_signal_threshold): # type: ignore
            signal = 'sell'
        else:
            signal = 'hold'
        print(f'signal:{signal}')
        
        if current_price > datainfo['previousclose']: # type: ignore
            rise_fall = 'rise'
        else:
            rise_fall = 'fall'
            print(f'rise/fall:{rise_fall}')
            
        
        
        time.sleep(60)  
