import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    all_period = len(data)
    data['Average_period'] = data['Close'].sum() / all_period
    return data


# def add_average_all_period(data):
#     window_size = len(data)
#     data['Average_period'] = data['Close'].rolling(window=window_size).mean()
#     return data


# af = fetch_stock_data(ticker="GOOGL", period='6mo')
# # # print(af)
# add = add_moving_average(data=af)
# print(add)