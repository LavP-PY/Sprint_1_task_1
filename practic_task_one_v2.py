import data_download as dd
import matplotlib.pyplot as plt
from practic_task_one import calculate_and_display_average_price as calc_ave
import pandas as pd

ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
period = input("Введите период для данных (например, '1mo' для одного месяца): ")

stock_data = dd.fetch_stock_data(ticker, period)
stock_data = dd.add_moving_average(stock_data)

def calculate_and_display_average_price_v2(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6)) # размеры (ширина и высота) диаграммы

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['Average_period'].values, label='Average all period')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Average_period'], label='Average all period')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart_with_average.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
    print(f'The average value for the selected period (Среднее значение за выбранный период): {calc_ave(data)}')

averenge = calculate_and_display_average_price_v2(data=stock_data, ticker=ticker, period=period)